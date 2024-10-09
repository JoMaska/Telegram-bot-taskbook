import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.config.config import Config, load_config

Config = load_config()

bot = Bot(Config.bot.token)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer("Test")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Exit")
        