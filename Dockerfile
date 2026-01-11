# Используем минимальный образ Python
FROM python:3.11-slim

# Устанавливаем системные зависимости для компиляции C-расширений
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только requirements.txt сначала (для кэширования слоя)
COPY requirements.txt .

# Устанавливаем Python зависимости ЯВНО, обновляем pip
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем весь исходный код
COPY . .

# Проверяем, что всё установилось правильно
RUN python -c "import pyrogram; print('Pyrogram version:', pyrogram.__version__)"

# Запускаем бота
CMD ["python", "-u", "bot.py"]
