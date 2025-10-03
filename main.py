import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Токен беремо з середовища Render (Environment Variables)
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт! Я Liora 🤍\n\nБот для авторського нагляду готовий до роботи.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
