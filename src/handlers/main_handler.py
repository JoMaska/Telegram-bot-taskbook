import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.inline_keyboard import get_main_inline_keyboard
from filters import IsAdminFilter

logger = logging.getLogger(__name__)

router = Router()

@router.message(~IsAdminFilter(), Command('start'))
async def start_cmd(msg: Message):
    await msg.answer('Test start command', reply_markup=get_main_inline_keyboard())

@router.message(Command('help'))
async def start_cmd(msg: Message):
    await msg.answer('Test help command')