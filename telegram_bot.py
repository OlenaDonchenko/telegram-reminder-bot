import telebot  # Імпортуємо бібліотеку

# 🔹 Введи свій API Token від @BotFather
TOKEN = "7809609243:AAGhiNcC-YBCA2tQVvqVmB5YtFLMyWjtQsI"

# 🔹 Введи Chat ID групи або каналу (знайди його через getUpdates)
CHAT_ID = "-1002587939007"

# Створюємо бота
bot = telebot.TeleBot(TOKEN)

# Надсилаємо тестове повідомлення
bot.send_message(CHAT_ID, "Привіт! Це тестове повідомлення від бота 🎉")

print("Повідомлення успішно надіслано!")
