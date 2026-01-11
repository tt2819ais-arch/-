import asyncio
import requests
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

BOT_TOKEN = "8397987541:AAHYDk99fAS5qp9Pi5nCOkXUdK4Eq5keiPY"
OPENROUTER_KEY = "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"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

SYSTEM_PROMPT = """
Ты — помощник, который пишет рефераты и конспекты в стиле обычного школьника
или студента. Текст должен звучать естественно, местами немного разговорно,
но без сленга. Избегай шаблонных фраз нейросетей, сложных конструкций,
формального академического стиля.

Пиши как человек, который объясняет тему своими словами. Можно использовать
простые связки, небольшие повторы и плавные переходы.

1 страница = примерно 1900 символов текста.
"""

def generate_text(topic: str, pages: int, title_page: str):
    target_symbols = pages * 1900

    prompt = (
        f"Титульный лист:\n{title_page}\n\n"
        f"Теперь напиши реферат на тему: '{topic}'. "
        f"Объём: около {target_symbols} символов. "
        "Стиль — как у обычного ученика или студента."
    )

    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    }

    r = requests.post("https://openrouter.ai/api/v1/chat/completions",
                      headers=headers, json=data)

    return r.json()["choices"][0]["message"]["content"]


def make_pdf(text: str, filename="referat.pdf"):
    styles = getSampleStyleSheet()
    story = []

    doc = SimpleDocTemplate(filename)

    parts = text.split("\n\n")

    for block in parts:
        if "Титульный лист" in block:
            story.append(Paragraph(block, styles["Title"]))
            story.append(PageBreak())
        else:
            story.append(Paragraph(block, styles["Normal"]))

    doc.build(story)
    return filename


@dp.message(F.text.startswith("/ref"))
async def ref_command(msg: Message):
    try:
        _, topic, pages, *title_text = msg.text.split(" ")
        pages = int(pages)
        title_page = " ".join(title_text)

        await msg.answer("Генерирую текст, подожди 5–10 секунд...")

        text = generate_text(topic, pages, title_page)
        file_path = make_pdf(text)

        await msg.answer_document(open(file_path, "rb"))

    except Exception as e:
        await msg.answer(f"Ошибка: {e}\n\nФормат:\n/ref <тема> <страницы> <титульный лист>")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
