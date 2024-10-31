import asyncio
import logging

from aiogram import Bot, Dispatcher

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config.config import load_config
from handlers import cmd_handler, callback_handler, admin_create_task_handler, user_handler, admin_delete_task_handler, echo_handler
from middlewares import DbSessionMiddleware

# from database.models import Base

logger = logging.getLogger(__name__)

async def main():
    
    config = load_config()
    
    engine = create_async_engine(config.db.url, echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    
    bot = Bot(config.bot.token)
    dp = Dispatcher()
    
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))
    
    dp.include_router(cmd_handler.router)
    dp.include_router(user_handler.router)
    dp.include_router(callback_handler.router)
    dp.include_router(admin_create_task_handler.admin_router)
    dp.include_router(admin_delete_task_handler.admin_router)
    dp.include_router(echo_handler.router)

    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
        
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Exit")
        