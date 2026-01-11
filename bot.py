import asyncio
import requests
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

TELEGRAM_TOKEN = "8397987541:AAHYDk99fAS5qp9Pi5nCOkXUdK4Eq5keiPY"
OPENROUTER_API_KEY = "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"
MODEL = "deepseek/deepseek-chat"

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()
router = Router()


def generate_text(topic, pages, title_page):
    try:
        pages = int(pages)
    except:
        return "Ошибка: количество страниц должно быть числом."

    words_per_page = 350
    target_words = pages * words_per_page

    prompt = f"""
Напиши реферат максимально естественно, как будто его писал ученик.
Тема: {topic}
Количество страниц: {pages} (примерно {target_words} слов)

Титульный лист, указанный пользователем:
{title_page}

Не используй AI-штампы, сложный академический стиль, канцелярит. 
Текст должен быть живым, простым, но грамотным.
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )
        resp = r.json()

        if "choices" in resp:
            return resp["choices"][0]["message"]["content"]
        else:
            return "Ошибка: Модель не вернула текст."
    except Exception as e:
        return f"Ошибка API: {e}"


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я бот для рефератов 😊\n\nФормат команды:\n/ref <тема> <страницы> <титульный лист>")


@router.message(Command("ref"))
async def ref(message: Message):
    try:
        parts = message.text.split(" ", 3)

        if len(parts) < 4:
            await message.answer("Ошибка!\n\nФормат:\n/ref <тема> <страницы> <титульный лист>")
            return

        topic = parts[1]
        pages = parts[2]
        title_page = parts[3]

        await message.answer("⏳ Генерирую реферат...")

        text = generate_text(topic, pages, title_page)

        await message.answer(text)

    except Exception as e:
        await message.answer(f"Ошибка обработки: {e}")


dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
