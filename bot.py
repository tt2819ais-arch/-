from pyrogram import Client, filters
from pyrogram.types import Message
import requests
import json
import asyncio
from datetime import datetime, timedelta

# Конфигурация
BOT_TOKEN = "8397987541:AAHYDk99fAS5qp9Pi5nCOkXUdK4Eq5keiPY"
OPENROUTER_API_KEY = "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"
API_ID = 22435995
API_HASH = "4c7b651950ed7f53520e66299453144d"

# Словари для хранения данных
user_sessions = {}  # Сессии авторизации пользователей
active_chats = set()  # ЛИЧНЫЕ ЧАТЫ с другими людьми, где включен AI

# Функция для создания сессии пользователя
def create_user_session(user_id):
    user_sessions[user_id] = {
        'phone_number': None,
        'phone_code_hash': None,
        'password_needed': False,
        'logged_in': False,
        'client': None,  # Это клиент пользователя (не бот!)
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
        
        print(f"OpenRouter статус: {response.status_code}")
        
        if response.status_code == 200:
            try:
                return response.json()["choices"][0]["message"]["content"]
            except (KeyError, IndexError) as e:
                print(f"Ошибка парсинга ответа: {e}")
                return "Ошибка: не удалось получить ответ AI."
        elif response.status_code == 401:
            return "❌ Ошибка: Неверный API ключ OpenRouter!"
        else:
            return f"❌ Ошибка AI API: {response.status_code}"
            
    except Exception as e:
        print(f"Ошибка: {e}")
        return f"❌ Ошибка подключения к AI"

# Создаем ТОЛЬКО бота (не пользовательский клиент пока)
bot_app = Client("telegram_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# ==============================================
# ОБРАБОТЧИКИ ДЛЯ БОТА (личные сообщения с ботом)
# ==============================================

# Команда /start в личных сообщениях с ботом
@bot_app.on_message(filters.command("start") & filters.private)
async def start_command(client, message: Message):
    cleanup_old_sessions()
    
    await message.reply(
        "👋 Добро пожаловать!\n\n"
        "📱 **Как работает AI бот:**\n"
        "1. Используйте /login чтобы авторизоваться\n"
        "2. После авторизации зайдите в ЛИЧНЫЙ ЧАТ с другим человеком\n"
        "3. Напишите `.старт` чтобы включить AI в ЭТОМ чате\n"
        "4. AI будет отвечать на сообщения в этом чате\n"
        "5. Напишите `.стоп` чтобы выключить AI\n\n"
        "🔧 **Команды для бота:**\n"
        "/login - Авторизация\n"
        "/logout - Выход\n"
        "/status - Статус\n"
        "/help - Помощь"
    )

# Команда /login - авторизация через бота
@bot_app.on_message(filters.command("login") & filters.private)
async def login_command(client, message: Message):
    user_id = message.from_user.id
    
    if user_id in user_sessions and user_sessions[user_id].get('logged_in'):
        await message.reply("✅ Вы уже авторизованы! Теперь можете использовать AI в личных чатах.")
        return
    
    # Создаем новую сессию
    session = create_user_session(user_id)
    
    await message.reply(
        "📱 **Введите номер телефона в международном формате:**\n"
        "Пример: `+79123456789`\n\n"
        "Для отмены отправьте /cancel"
    )

# Обработка ввода в личных сообщениях с ботом
@bot_app.on_message(filters.text & filters.private)
async def handle_bot_messages(client, message: Message):
    user_id = message.from_user.id
    text = message.text.strip()
    
    # Если это не команда бота и пользователь не в процессе авторизации
    if (not text.startswith('/') and 
        user_id not in user_sessions and 
        text not in ['.старт', '.стоп', '.start', '.stop']):
        return
    
    # Отмена операции
    if text.lower() == "/cancel":
        if user_id in user_sessions:
            if user_sessions[user_id]['client']:
                try:
                    await user_sessions[user_id]['client'].disconnect()
                except:
                    pass
            del user_sessions[user_id]
        await message.reply("❌ Операция отменена.")
        return
    
    # Если пользователь не в процессе авторизации
    if user_id not in user_sessions:
        # Это команды бота
        if text.lower() in ["/help", "/помощь"]:
            await start_command(client, message)
        elif text.lower() in ["/status", "/статус"]:
            await status_command(client, message)
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
            # Создаем клиент для пользователя (это важно!)
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
    elif (session['phone_number'] and 
          session['phone_code_hash'] and 
          not session['password_needed'] and 
          not session.get('logged_in')):
        try:
            code = text
            
            # Пытаемся авторизоваться
            try:
                await session['client'].sign_in(
                    phone_number=session['phone_number'],
                    phone_code_hash=session['phone_code_hash'],
                    phone_code=code
                )
                
                session['logged_in'] = True
                await message.reply(
                    "✅ **Авторизация успешна!**\n\n"
                    "**Теперь как использовать AI:**\n"
                    "1. Откройте личный чат с другим человеком\n"
                    "2. Напишите `.старт` в этом чате\n"
                    "3. AI будет отвечать на сообщения в этом чате\n"
                    "4. Напишите `.стоп` чтобы выключить\n\n"
                    "⚠️ **ВАЖНО:** Бот должен быть добавлен в чат!"
                )
                
            except Exception as e:
                if "SESSION_PASSWORD_NEEDED" in str(e):
                    # Запрашиваем пароль 2FA
                    session['password_needed'] = True
                    await message.reply(
                        "🔐 **Требуется пароль 2FA**\n\n"
                        "Введите пароль от вашего аккаунта Telegram:"
                    )
                else:
                    raise e
                
        except Exception as e:
            error_msg = str(e)
            await message.reply(f"❌ Ошибка авторизации: {error_msg}")
            if user_id in user_sessions:
                del user_sessions[user_id]
    
    # Если нужен пароль 2FA
    elif session['password_needed'] and not session.get('logged_in'):
        try:
            password = text
            
            # Проверяем пароль
            await session['client'].check_password(password=password)
            
            session['logged_in'] = True
            session['password_needed'] = False
            
            await message.reply(
                "✅ **Авторизация успешна!**\n\n"
                "**Теперь как использовать AI:**\n"
                "1. Откройте личный чат с другим человеком\n"
                "2. Напишите `.старт` в этом чате\n"
                "3. AI будет отвечать на сообщения в этом чате\n"
                "4. Напишите `.стоп` чтобы выключить\n\n"
                "⚠️ **ВАЖНО:** Бот должен быть добавлен в чат!"
            )
            
        except Exception as e:
            error_msg = str(e)
            if "PASSWORD_HASH_INVALID" in str(e):
                await message.reply("❌ Неверный пароль. Попробуйте еще раз:")
            else:
                await message.reply(f"❌ Ошибка: {error_msg}")
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
    
    await message.reply("✅ Вы успешно вышли из системы.")

# Команда /status
@bot_app.on_message(filters.command("status") & filters.private)
async def status_command(client, message: Message):
    user_id = message.from_user.id
    
    status_text = f"👤 **ID пользователя:** {user_id}\n"
    
    if user_id in user_sessions and user_sessions[user_id].get('logged_in'):
        status_text += "🔓 **Авторизация:** ✅\n"
        status_text += f"📱 **Номер:** {user_sessions[user_id]['phone_number']}\n"
        
        # Считаем активные чаты этого пользователя
        user_active_chats = [chat_id for chat_id in active_chats]
        status_text += f"💬 **Активных чатов с AI:** {len(user_active_chats)}\n"
    else:
        status_text += "🔒 **Авторизация:** ❌\n"
    
    await message.reply(status_text)

# ==============================================
# ОБРАБОТЧИКИ ДЛЯ ПОЛЬЗОВАТЕЛЬСКОГО КЛИЕНТА 
# (работает в личных чатах с другими людьми)
# ==============================================

# Функция для запуска пользовательского клиента
async def run_user_client(user_id):
    if user_id not in user_sessions or not user_sessions[user_id].get('logged_in'):
        return None
    
    session = user_sessions[user_id]
    
    # Обработчик для команд .старт/.стоп в личных чатах
    @session['client'].on_message(filters.text & filters.private & ~filters.me)
    async def handle_user_messages(client, message: Message):
        chat_id = message.chat.id
        text = message.text.strip().lower()
        
        print(f"Пользователь {user_id} в чате {chat_id}: {text}")
        
        # Команды управления AI
        if text == ".старт" or text == ".start":
            active_chats.add(chat_id)
            await message.reply("✅ AI включен в этом чате! Я буду отвечать на сообщения.")
        
        elif text == ".стоп" or text == ".stop":
            active_chats.discard(chat_id)
            await message.reply("✅ AI выключен в этом чате.")
        
        # Если AI включен в этом чате и это не команда
        elif chat_id in active_chats and not text.startswith('.'):
            try:
                # Отвечаем от имени пользователя через AI
                response = get_ai_response(message.text)
                await message.reply(f"🤖 {response}")
            except Exception as e:
                print(f"Ошибка AI в чате {chat_id}: {e}")
                await message.reply("❌ Ошибка AI")

    # Запускаем пользовательский клиент
    try:
        if not session['client'].is_connected:
            await session['client'].start()
        return session['client']
    except Exception as e:
        print(f"Ошибка запуска клиента для {user_id}: {e}")
        return None

# Запуск бота и всех пользовательских клиентов
async def main():
    # Запускаем бота
    await bot_app.start()
    print("🤖 Бот запущен!")
    
    # Запускаем пользовательские клиенты для авторизованных пользователей
    for user_id in list(user_sessions.keys()):
        if user_sessions[user_id].get('logged_in') and user_sessions[user_id]['client']:
            try:
                await run_user_client(user_id)
                print(f"👤 Клиент для пользователя {user_id} запущен")
            except Exception as e:
                print(f"❌ Ошибка запуска клиента {user_id}: {e}")
    
    # Ждем
    await asyncio.Event().wait()

# Запуск
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⏹️ Бот остановлен")
