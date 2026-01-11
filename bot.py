import asyncio
import json
import requests
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# ---------- ТОКЕНЫ ----------
BOT_TOKEN = "8397987541:AAHYDk99fAS5qp9Pi5nCOkXUdK4Eq5keiPY"
OPENROUTER_API_KEY = "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"
MODEL_NAME = "meta-llama/llama-3.3-70b-instruct:free"

# ---------- ИНИЦИАЛИЗАЦИЯ ----------
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()

# ---------- СОСТОЯНИЯ FSM ----------
class RefStates(StatesGroup):
    school = State()
    group_class = State()
    student_name = State()
    teacher_name = State()
    topic = State()
    pages = State()

# ---------- ФУНКЦИЯ ГЕНЕРАЦИИ ТЕКСТА ----------
def generate_text(topic: str, pages: int, title_page: str) -> str:
    try:
        pages = int(pages)
    except:
        return "Ошибка: количество страниц должно быть числом."

    words_per_page = 350
    target_words = pages * words_per_page

    prompt = f"""
Напиши реферат максимально естественно, как будто его писал ученик.
Тема: {topic}
Количество страниц: {pages} (~{target_words} слов)

Титульный лист:
{title_page}

Не используй AI-штампы, сложный академический стиль, канцелярит. 
Текст должен быть живым и человечным.
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "provider": {"sort": "throughput"}
    }

    try:
        r = requests.post("https://openrouter.ai/api/v1/chat/completions",
                          headers=headers, data=json.dumps(data))
        resp = r.json()

        if "choices" in resp and len(resp["choices"]) > 0:
            return resp["choices"][0]["message"]["content"]
        else:
            return "Ошибка OpenRouter:\n" + json.dumps(resp, ensure_ascii=False, indent=2)

    except Exception as e:
        return f"Ошибка API: {e}"

# ---------- ФУНКЦИЯ СОЗДАНИЯ PDF ----------
def make_pdf(text: str) -> BytesIO:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    story = []

    for block in text.split("\n"):
        if block.strip().lower().startswith("титульный лист"):
            story.append(Paragraph(block, styles["Title"]))
            story.append(PageBreak())
        else:
            story.append(Paragraph(block, styles["Normal"]))

    doc.build(story)
    buffer.seek(0)
    return buffer

# ---------- /start ----------
@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот для интерактивного создания рефератов.\n"
                         "Нажми /ref чтобы начать процесс генерации.")

# ---------- /ref (начало диалога) ----------
@router.message(Command("ref"))
async def ref_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Сначала заполним титульный лист.\n\nВведите название учебного заведения:")
    await state.set_state(RefStates.school)

# ---------- ШАГ 1: школа ----------
@router.message(RefStates.school)
async def step_school(message: types.Message, state: FSMContext):
    await state.update_data(school=message.text)
    await message.answer("Введите группу или класс:")
    await state.set_state(RefStates.group_class)

# ---------- ШАГ 2: группа/класс ----------
@router.message(RefStates.group_class)
async def step_group(message: types.Message, state: FSMContext):
    await state.update_data(group_class=message.text)
    await message.answer("Введите ФИО ученика:")
    await state.set_state(RefStates.student_name)

# ---------- ШАГ 3: ФИО ученика ----------
@router.message(RefStates.student_name)
async def step_student(message: types.Message, state: FSMContext):
    await state.update_data(student_name=message.text)
    await message.answer("Введите ФИО преподавателя:")
    await state.set_state(RefStates.teacher_name)

# ---------- ШАГ 4: ФИО преподавателя ----------
@router.message(RefStates.teacher_name)
async def step_teacher(message: types.Message, state: FSMContext):
    await state.update_data(teacher_name=message.text)
    await message.answer("Введите тему реферата:")
    await state.set_state(RefStates.topic)

# ---------- ШАГ 5: тема ----------
@router.message(RefStates.topic)
async def step_topic(message: types.Message, state: FSMContext):
    await state.update_data(topic=message.text)
    await message.answer("Сколько страниц сделать?")
    await state.set_state(RefStates.pages)

# ---------- ШАГ 6: страницы и генерация ----------
@router.message(RefStates.pages)
async def step_pages(message: types.Message, state: FSMContext):
    try:
        pages = int(message.text)
    except:
        await message.answer("Введите число страниц цифрами!")
        return

    data = await state.get_data()
    school = data["school"]
    group = data["group_class"]
    student = data["student_name"]
    teacher = data["teacher_name"]
    topic = data["topic"]

    # Формируем титульный лист
    title_page = f"Учебное заведение: {school}\nКласс/Группа: {group}\nУченик: {student}\nПреподаватель: {teacher}"

    await message.answer("⏳ Генерирую реферат... Это может занять 10–20 секунд.")

    # Генерация текста
    text = generate_text(topic, pages, title_page)
    pdf_file = make_pdf(text)

    await message.answer_document(document=pdf_file, filename="referat.pdf")
    await state.clear()

# ---------- ИНИЦИАЛИЗАЦИЯ РОУТЕРОВ ----------
dp.include_router(router)

# ---------- ЗАПУСК ----------
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
