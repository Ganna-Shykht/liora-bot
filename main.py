import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Set it in Render → Environment.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт! Я Liora 🤍\nБот для авторського нагляду готовий до роботи.")
    logging.info("Handled /start or /help from %s", message.from_user.id)

# На всякий випадок відповімо на будь-який текст — щоб перевірити, що апдейти приходять
@dp.message_handler()
async def echo_all(message: types.Message):
    await message.reply("Я на зв'язку ✅")
    logging.info("Echoed a message from %s", message.from_user.id)

if __name__ == '__main__':
    logging.info("Starting polling…")
    executor.start_polling(dp, skip_updates=True)
