
import os
import logging
from aiogram import Bot, Dispatcher, types, executor

# Замість токена напряму — використовуємо змінну оточення
API_TOKEN = os.getenv("API_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт! Я твій бот для мінікурсів. Пиши, якщо маєш питання 😉")

@dp.message_handler()
async def handle_message(message: types.Message):
    # Просто пересилає все, що пишуть, адміну
    if ADMIN_ID:
        await bot.send_message(chat_id=ADMIN_ID, text=f"Новий запит від @{message.from_user.username or 'невідомо'}:\n{message.text}")
    await message.answer("Дякую за повідомлення! Я на зв'язку 😊")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
