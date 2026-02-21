# main.py

import telebot

# ✅ Token va Admin ID
TOKEN = "8599100876:AAGhk-U0gLCKNUAEf5Q1qThzsaAH-WHYmmA"
ADMIN_ID = 7257755738  # O‘zing Telegram ID

# Botni yaratish
bot = telebot.TeleBot(TOKEN)

# /start komandaga javob
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Kino botga xush kelibsiz 🎬")

# Foydalanuvchi kod yuborsa javob (minimal misol)
@bot.message_handler(func=lambda message: True)
def echo_code(message):
    text = message.text
    # Minimal: foydalanuvchi yozganini qaytaradi
    bot.reply_to(message, f"Siz yozdingiz: {text}\n(Bu yerga kino kodi funksiyasi yoziladi)")

# Botni ishga tushirish
bot.polling()
