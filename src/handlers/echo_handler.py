import logging

from aiogram import Router
from aiogram.types import Message

logger = logging.getLogger(__name__)

router = Router()

@router.message()
async def echo_cmd(msg: Message):
    await msg.answer('Неизвестная команда')