import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.inline_keyboards import get_main_inline_keyboard

logger = logging.getLogger(__name__)

router = Router()

@router.message(Command('start'))
async def start_cmd(msg: Message):
    await msg.answer('Test start command', reply_markup=get_main_inline_keyboard())

@router.message(Command('help'))
async def start_cmd(msg: Message):
    await msg.answer('Test help command')