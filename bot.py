import random
import logging
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

# Встановіть свій токен бота
TOKEN = "7711155592:AAEvu3h08FioqRl6ROSj6ihN8DPOk2M0gRU"
CHAT_ID = "6774448304"  # ID чату, куди бот надсилатиме повідомлення

# Список компліментів
COMPLIMENTS = [
    "Ти неймовірний!",
    "Ти робиш світ кращим!",
    "Твоя усмішка заряджає енергією!",
    "Ти дуже талановитий!",
    "Ти завжди знаходиш рішення у будь-якій ситуації!",
    "З тобою завжди цікаво!",
    "Твій оптимізм надихає!"
]

# Налаштування логування
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)

async def send_compliment():
    """Функція для надсилання випадкового компліменту"""
    compliment = random.choice(COMPLIMENTS)
    await bot.send_message(chat_id=CHAT_ID, text=compliment)

async def main():
    scheduler = AsyncIOScheduler()
    for hour in range(7, 24):  # З 07:00 до 23:00 (бо 00:00 вже не входить)
        scheduler.add_job(send_compliment, "interval", seconds=10)

    
    scheduler.start()
    while True:


        
        await asyncio.sleep(3600)  # Підтримуємо програму в активному стані

if __name__ == "__main__":
    asyncio.run(main())
