import logging

from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery

logger = logging.getLogger(__name__)

router = Router()

@router.callback_query(F.data == "test_task")
async def callback_query_handler(callback: CallbackQuery, bot: Bot):
    await bot.send_message(text='test task', chat_id=callback.from_user.id)
    await callback.answer()

@router.callback_query(F.data == "practical_task")
async def callback_query_handler(callback: CallbackQuery, bot: Bot):
    await bot.send_message(text='practical task', chat_id=callback.from_user.id)
    await callback.answer()