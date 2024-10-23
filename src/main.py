import asyncio
import logging

from aiogram import Bot, Dispatcher

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config.config import load_config
from handlers import main_handler, callback_handler
from middlewares import DbSessionMiddleware

logger = logging.getLogger(__name__)

async def main():
    
    config = load_config()
    
    engine = create_async_engine(config.db.url, echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    bot = Bot(config.bot.token)
    dp = Dispatcher()
    
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))
    
    dp.include_router(main_handler.router)
    dp.include_router(callback_handler.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Exit")
        