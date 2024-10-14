import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.config.config import Config, load_config

from src.handlers import main_handler

logger = logging.getLogger(__name__)

async def main():
    Config = load_config()

    bot = Bot(Config.bot.token)
    dp = Dispatcher()
    
    dp.include_router(main_handler.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Exit")
        