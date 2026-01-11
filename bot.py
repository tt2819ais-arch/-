import requests
import json

OPENROUTER_API_KEY = "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"
MODEL = "deepseek/deepseek-chat"  # или любая другая модель OpenRouter

def generate_text(topic, pages, title_page):
    # Безопасная обработка числа страниц
    try:
        pages = int(pages)
    except:
        return "Ошибка: количество страниц должно быть числом."

    # Примерный подсчёт слов на “ученическую страницу”
    words_per_page = 350
    target_words = pages * words_per_page

    prompt = f"""
Тебе нужно написать реферат так, чтобы он выглядел как будто его писал реальный ученик, без типичного AI-стиля. 
Избегай канцелярита, супер-правильных формулировок и идеально литературной речи.

Формат:
1) Титульный лист (данные пользователя):
{title_page}

2) Основная часть.
Объём: примерно {pages} страниц ({target_words} слов).
Тема реферата: "{topic}"

Требования:
- текст должен быть естественным, местами простым, как будто студент писал своими словами;
- не используй фразы: "как модель искусственного интеллекта", "в заключение можно сказать", "данный текст";
- используй лёгкий пересказ, примеры, объяснения, но без академического тона;
- допускаются мелкие шероховатости, чтобы текст звучал живым;
- структура: введение → раскрытие темы → вывод.

Теперь напиши готовый реферат.
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
        r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response = r.json()

        # Универсальное получение текста
        if "choices" in response and len(response["choices"]) > 0:
            text = response["choices"][0]["message"]["content"]
        else:
            text = "Ошибка: Модель не вернула текст. Ответ:\n" + json.dumps(response, ensure_ascii=False)

        return text

    except Exception as e:
        return f"Ошибка при запросе к API: {e}"
