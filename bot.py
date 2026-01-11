from pyrogram import Client, filters
from pyrogram.types import Message
import requests
import json
import asyncio
from datetime import datetime, timedelta

# Конфигурация Telegram бота
BOT_TOKEN = "8397987541:AAHYDk99fAS5qp9Pi5nCOkXUdK4Eq5keiPY"
OPENROUTER_API_KEY = "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"
API_ID = 22435995
API_HASH = "4c7b651950ed7f53520e66299453144d"

# Словари для хранения данных
user_sessions = {}  # Сессии авторизации пользователей
active_users = set()  # Пользователи с включенным AI в личных сообщениях

# Функция для создания сессии пользователя
def create_user_session(user_id):
    user_sessions[user_id] = {
        'phone_number': None,
        'phone_code_hash': None,
        'logged_in': False,
        'client': None,
        'created_at': datetime.now()
    }
    return user_sessions[user_id]

# Функция для очистки старых сессий
def cleanup_old_sessions():
    current_time = datetime.now()
    expired_users = []
    
    for user_id, session in user_sessions.items():
        if current_time - session['created_at'] > timedelta(hours=1):
            expired_users.append(user_id)
    
    for user_id in expired_users:
        if user_id in user_sessions:
            if user_sessions[user_id]['client']:
                try:
                    user_sessions[user_id]['client'].disconnect()
                except:
                    pass
            del user_sessions[user_id]
            if user_id in active_users:
                active_users.remove(user_id)

# Функция для общения с OpenRouter AI
def get_ai_response(user_message):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://t.me/",
        "X-Title": "Telegram AI Bot"
    }
    data = {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ],
        "provider": {
            "sort": "throughput"
        }
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=30)
        if response.status_code == 200:
            try:
                return response.json()["choices"][0]["message"]["content"]
            except (KeyError, IndexError) as e:
                print(f"Ошибка парсинга ответа: {e}")
                return "Ошибка: не удалось получить ответ AI."
        else:
            print(f"Ошибка API: {response.status_code}, {response.text}")
            return f"Ошибка AI API: {response.status_code}"
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return f"Ошибка подключения к AI: {str(e)}"

# Создаем бота
bot_app = Client("telegram_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Команда /start
@bot_app.on_message(filters.command("start") & filters.private)
async def start_command(client, message: Message):
    cleanup_old_sessions()
    
    await message.reply(
        "👋 Добро пожаловать в AI бота!\n\n"
        "📱 **Для начала работы:**\n"
        "1. Используйте /login для авторизации по номеру телефона\n"
        "2. После авторизации используйте `.старт` чтобы включить AI\n"
        "3. Начните общаться с AI\n"
        "4. Используйте `.стоп` чтобы выключить AI\n\n"
        "🔧 **Доступные команды:**\n"
        "/login - Авторизация\n"
        "/logout - Выход\n"
        "/status - Статус\n"
        "/ai [запрос] - Тест AI"
    )

# Команда /login - авторизация по номеру телефона
@bot_app.on_message(filters.command("login") & filters.private)
async def login_command(client, message: Message):
    user_id = message.from_user.id
    
    if user_id in user_sessions and user_sessions[user_id].get('logged_in'):
        await message.reply("✅ Вы уже авторизованы!")
        return
    
    # Создаем новую сессию
    session = create_user_session(user_id)
    
    await message.reply(
        "📱 **Введите номер телефона в международном формате:**\n"
        "Пример: `+79123456789`\n\n"
        "Для отмены отправьте /cancel"
    )

# Обработка ввода номера телефона и кода
@bot_app.on_message(filters.text & filters.private)
async def handle_input(client, message: Message):
    user_id = message.from_user.id
    text = message.text.strip()
    
    # Отмена операции
    if text.lower() == "/cancel":
        if user_id in user_sessions:
            if user_sessions[user_id]['client']:
                try:
                    await user_sessions[user_id]['client'].disconnect()
                except:
                    pass
            del user_sessions[user_id]
        if user_id in active_users:
            active_users.remove(user_id)
        await message.reply("❌ Операция отменена.")
        return
    
    # Если пользователь не в процессе авторизации
    if user_id not in user_sessions:
        # Проверяем команды управления AI
        if text.lower() == ".старт":
            if user_id in user_sessions and user_sessions[user_id].get('logged_in'):
                active_users.add(user_id)
                await message.reply("✅ AI включен! Теперь я буду отвечать на ваши сообщения.\n\nОтправьте `.стоп` чтобы выключить.")
            else:
                await message.reply("❌ Сначала авторизуйтесь через /login")
            return
        elif text.lower() == ".стоп":
            if user_id in active_users:
                active_users.remove(user_id)
                await message.reply("✅ AI выключен. Отправьте `.старт` чтобы включить снова.")
            else:
                await message.reply("ℹ️ AI уже выключен.")
            return
        # Если это обычное сообщение и AI включен
        elif user_id in active_users:
            # Отвечаем через AI
            await message.reply("🤔 Думаю...")
            response = get_ai_response(text)
            await message.reply(f"🤖 {response}")
            return
        else:
            return
    
    session = user_sessions[user_id]
    
    # Если номер телефона еще не введен
    if not session['phone_number'] and not session.get('logged_in'):
        phone_number = text
        
        # Валидация номера
        if not phone_number.startswith('+') or len(phone_number) < 10:
            await message.reply("❌ Неверный формат. Пример: `+79123456789`")
            return
        
        session['phone_number'] = phone_number
        
        try:
            # Создаем клиент для пользователя
            client_name = f"user_session_{user_id}"
            user_client = Client(
                client_name,
                api_id=API_ID,
                api_hash=API_HASH,
                in_memory=True
            )
            
            # Запрашиваем код
            await user_client.connect()
            sent_code = await user_client.send_code(phone_number)
            session['phone_code_hash'] = sent_code.phone_code_hash
            session['client'] = user_client
            
            await message.reply(
                "📨 **Код отправлен на ваш номер телефона.**\n"
                "Введите код в формате: `12345`\n\n"
                "Для отмены отправьте /cancel"
            )
            
        except Exception as e:
            error_msg = str(e)
            await message.reply(f"❌ Ошибка: {error_msg}")
            if user_id in user_sessions:
                del user_sessions[user_id]
    
    # Если вводится код подтверждения
    elif session['phone_number'] and session['phone_code_hash'] and not session.get('logged_in'):
        try:
            code = text
            
            # Авторизуемся
            await session['client'].sign_in(
                phone_number=session['phone_number'],
                phone_code_hash=session['phone_code_hash'],
                phone_code=code
            )
            
            session['logged_in'] = True
            await message.reply(
                "✅ **Авторизация успешна!**\n\n"
                "Теперь вы можете использовать AI:\n"
                "• `.старт` - включить AI\n"
                "• `.стоп` - выключить AI\n"
                "• После включения просто пишите сообщения и AI будет отвечать\n\n"
                "Используйте `/logout` для выхода."
            )
            
        except Exception as e:
            error_msg = str(e)
            await message.reply(f"❌ Ошибка авторизации: {error_msg}")
            if user_id in user_sessions:
                del user_sessions[user_id]

# Команда /logout
@bot_app.on_message(filters.command("logout") & filters.private)
async def logout_command(client, message: Message):
    user_id = message.from_user.id
    
    if user_id in user_sessions:
        if user_sessions[user_id]['client']:
            try:
                await user_sessions[user_id]['client'].disconnect()
            except:
                pass
        del user_sessions[user_id]
    
    if user_id in active_users:
        active_users.remove(user_id)
    
    await message.reply("✅ Вы успешно вышли из системы.")

# Команда /status
@bot_app.on_message(filters.command("status") & filters.private)
async def status_command(client, message: Message):
    user_id = message.from_user.id
    
    status_text = f"👤 **ID пользователя:** {user_id}\n"
    
    if user_id in user_sessions and user_sessions[user_id].get('logged_in'):
        status_text += "🔓 **Авторизация:** ✅\n"
    else:
        status_text += "🔒 **Авторизация:** ❌\n"
    
    if user_id in active_users:
        status_text += "🤖 **AI статус:** Включен\n"
        status_text += "📝 Просто пишите сообщения и я буду отвечать!"
    else:
        status_text += "🤖 **AI статус:** Выключен\n"
        status_text += "💡 Используйте `.старт` чтобы включить AI"
    
    await message.reply(status_text)

# Команда /ai для тестирования
@bot_app.on_message(filters.command("ai") & filters.private)
async def ai_test_command(client, message: Message):
    user_id = message.from_user.id
    
    if user_id not in user_sessions or not user_sessions[user_id].get('logged_in'):
        await message.reply("❌ Сначала авторизуйтесь через /login")
        return
    
    # Получаем текст запроса
    query = message.text.split(' ', 1)
    if len(query) < 2:
        await message.reply("❌ Введите запрос после команды /ai\nПример: `/ai Привет, как дела?`")
        return
    
    user_message = query[1]
    await message.reply("🤔 Думаю...")
    
    response = get_ai_response(user_message)
    await message.reply(f"🤖 {response}")

# Запуск бота
print("🤖 Бот запускается...")
bot_app.run()
