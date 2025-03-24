import asyncio
import logging
from aiogram import Bot, Dispatcher
import schedule

# 🔹 Введи свій API Token від BotFather
TOKEN = "7809609243:AAGhiNcC-YBCA2tQVvqVmB5YtFLMyWjtQsI"  # Замінити на твій токен

# 🔹 Введи Chat ID групи або каналу
CHAT_ID = "-1002587939007"  # Замінити на правильний ID

# 🔹 Створюємо об'єкт бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# 🔹 Логування (для дебагу)
logging.basicConfig(level=logging.INFO)

# 🔹 Функція для ранкового нагадування
async def morning_message():
    await bot.send_message(CHAT_ID, "🌞 Morgendliche Erinnerung:\n"
                                    "Guten Morgen! Ein neuer Tag – neue Möglichkeiten! 📚✨\n"
                                    "Vergiss nicht zu lernen: Jeder kleine Schritt heute bringt dich großen Erfolgen näher. 🚀\n"
                                    "Viel Erfolg! 💪")

# 🔹 Функція для вечірнього нагадування
async def evening_message():
    await bot.send_message(CHAT_ID, "🌙 Abendliche Erinnerung:\n"
                                    "Der Tag geht zu Ende, aber dein Wissen wächst! 📖🔍\n"
                                    "Mache eine kurze Wiederholung, um das Gelernte zu festigen. Kleine Anstrengungen jeden Tag führen zu großem Erfolg morgen!\n"
                                    "Gute Nacht! 😴💡")

# 🔹 Додаємо розклад
schedule.every().day.at("09:00").do(lambda: asyncio.create_task(morning_message()))
schedule.every().day.at("20:00").do(lambda: asyncio.create_task(evening_message()))

# 🔹 Основний цикл для виконання розкладу
async def scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(60)  # Чекає 60 секунд перед наступною перевіркою

# 🔹 Головна функція запуску бота
async def main():
    asyncio.create_task(scheduler())  # Запускає розклад у фоновому режимі
    await dp.start_polling(bot)  # Запускає бота

# 🔹 Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
