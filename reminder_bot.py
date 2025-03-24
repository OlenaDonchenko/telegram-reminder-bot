import telebot
import schedule
import time

# 🔹 Введи свій API Token від BotFather
TOKEN = "7809609243:AAGhiNcC-YBCA2tQVvqVmB5YtFLMyWjtQsI"  # Замінити на твій токен

# 🔹 Введи Chat ID групи або каналу
CHAT_ID = "-1002587939007"  # Замінити на правильний ID

# 🔹 Створюємо об'єкт бота
bot = telebot.TeleBot(TOKEN)

# 🔹 Функція для ранкового нагадування
def morning_message():
    bot.send_message(CHAT_ID, "🌞 Morgendliche Erinnerung:
Guten Morgen! Ein neuer Tag – neue Möglichkeiten! 📚✨
Vergiss nicht zu lernen: Jeder kleine Schritt heute bringt dich großen Erfolgen näher. 🚀
Viel Erfolg! 💪")

# 🔹 Функція для вечірнього нагадування
def evening_message():
    bot.send_message(CHAT_ID, "🌙 Abendliche Erinnerung:
Der Tag geht zu Ende, aber dein Wissen wächst! 📖🔍
Mache eine kurze Wiederholung, um das Gelernte zu festigen. Kleine Anstrengungen jeden Tag führen zu großem Erfolg morgen!
Gute Nacht! 😴💡")

# 🔹 Додаємо розклад
schedule.every().day.at("09:00").do(morning_message)  # Повідомлення о 09:00
schedule.every().day.at("20:00").do(evening_message)  # Повідомлення о 20:00

# 🔹 Основний цикл для виконання розкладу
while True:
    schedule.run_pending()  # Перевіряє, чи настав час для відправки повідомлення
    time.sleep(60)  # Чекає 60 секунд перед наступною перевіркою

