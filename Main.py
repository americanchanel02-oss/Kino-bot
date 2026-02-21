TOKEN = "SENING_BOT_TOKEN"   #8599100876:AAGhk-U0gLCKNUAEf5Q1qThzsaAH-WHYmmA
ADMIN_ID = 123456789         #7257755738

# import telebot

bot = telebot.TeleBot(TOKEN)

# Foydalanuvchi /start yuborsa xabar
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Kino botga xush kelibsiz 🎬")

bot.polling()Bu yerga Telegram bot kodi yoziladi
