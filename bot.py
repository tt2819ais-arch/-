from pyrogram import Client, filters
from pyrogram.types import Message
import requests
import json
import asyncio
from datetime import datetime, timedelta

# === КОНФИГ ===
BOT_TOKEN = "8397987541:AAHYDk99fAS5qp9Pi5nCOkXUdK4Eq5keiPY"
OPENROUTER_API_KEY = "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"
API_ID = 22435995
API_HASH = "4c7b651950ed7f53520e66299453144d"

# === ХРАНИЛИЩЕ ===
# user_id: {"phone": "+7912...", "client": Client, "logged_in": True, "active_chats": set()}
user_sessions = {}

# === AI ФУНКЦИЯ ===
def get_ai_response(text):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [{"role": "user", "content": text}]
    }
    try:
        resp = requests.post(url, headers=headers, json=data, timeout=30)
        return resp.json()["choices"][0]["message"]["content"]
    except:
        return "Ошибка AI"

# === ГЛАВНЫЙ КЛИЕНТ (БОТ + ПОЛЬЗОВАТЕЛЬ) ===
app = Client("my_account", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# === КОМАНДА /start ===
@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    await message.reply(
        "👋 AI-бот\n"
        "1. /login - авторизация по номеру\n"
        "2. После авторизации иди в ЛИЧНЫЙ чат\n"
        "3. Напиши `.старт` - AI включится в этом чате\n"
        "4. Напиши `.стоп` - AI выключится"
    )

# === КОМАНДА /login ===
@app.on_message(filters.command("login") & filters.private)
async def login_cmd(client, message):
    user_id = message.from_user.id
    user_sessions[user_id] = {
        "phone": None,
        "code_hash": None,
        "step": "wait_phone"
    }
    await message.reply("📱 Отправь номер телефона (+79123456789):")

# === ОБРАБОТКА СООБЩЕНИЙ ===
@app.on_message(filters.text & filters.private)
async def handle_all_messages(client, message):
    user_id = message.from_user.id
    text = message.text.strip()
    
    # === ЕСЛИ ЭТО ЧАТ С ДРУГИМ ЧЕЛОВЕКОМ ===
    if message.chat.id != user_id:  # Это не личка с ботом, а чат с другим человеком
        if text.lower() == ".старт":
            if user_id not in user_sessions:
                return
            if "active_chats" not in user_sessions[user_id]:
                user_sessions[user_id]["active_chats"] = set()
            user_sessions[user_id]["active_chats"].add(message.chat.id)
            await message.reply("✅ AI включен в этом чате!")
            return
        
        elif text.lower() == ".стоп":
            if user_id in user_sessions and "active_chats" in user_sessions[user_id]:
                user_sessions[user_id]["active_chats"].discard(message.chat.id)
                await message.reply("✅ AI выключен.")
            return
        
        # Если AI включен в этом чате
        if (user_id in user_sessions and 
            "active_chats" in user_sessions[user_id] and 
            message.chat.id in user_sessions[user_id]["active_chats"]):
            ai_response = get_ai_response(text)
            await message.reply(f"🤖 {ai_response}")
            return
    
    # === ЕСЛИ ЭТО ЛИЧКА С БОТОМ (авторизация) ===
    if user_id not in user_sessions:
        return
    
    session = user_sessions[user_id]
    
    # Шаг 1: Ожидаем номер
    if session["step"] == "wait_phone" and text.startswith("+"):
        session["phone"] = text
        session["step"] = "wait_code"
        
        try:
            # Отправляем код
            sent_code = await client.send_code(text)
            session["code_hash"] = sent_code.phone_code_hash
            await message.reply("📨 Код отправлен. Введи код:")
        except Exception as e:
            await message.reply(f"❌ Ошибка: {e}")
            del user_sessions[user_id]
    
    # Шаг 2: Ожидаем код
    elif session["step"] == "wait_code" and text.isdigit():
        try:
            # Авторизуемся
            await client.sign_in(
                phone_number=session["phone"],
                phone_code_hash=session["code_hash"],
                phone_code=text
            )
            
            session["step"] = "logged_in"
            session["active_chats"] = set()
            await message.reply(
                "✅ Авторизация успешна!\n\n"
                "Теперь иди в личный чат с человеком и напиши `.старт`\n"
                "AI будет отвечать на все сообщения в том чате."
            )
        except Exception as e:
            if "SESSION_PASSWORD_NEEDED" in str(e):
                session["step"] = "wait_password"
                await message.reply("🔐 Введи пароль 2FA:")
            else:
                await message.reply(f"❌ Ошибка: {e}")
                del user_sessions[user_id]
    
    # Шаг 3: Ожидаем пароль 2FA
    elif session["step"] == "wait_password":
        try:
            await client.check_password(password=text)
            session["step"] = "logged_in"
            session["active_chats"] = set()
            await message.reply(
                "✅ Авторизация успешна!\n\n"
                "Теперь иди в личный чат с человеком и напиши `.старт`"
            )
        except:
            await message.reply("❌ Неверный пароль. Попробуй еще раз:")

# === ЗАПУСК ===
print("🤖 БОТ ЗАПУСКАЕТСЯ...")
app.run()
