import logging
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import src.keyboards.inline_keyboards as kb

router = Router()

logger = logging.getLogger(__name__)

@router.message(Command('start'))
async def start_cmd(msg: Message):
    await msg.answer('Test start command', reply_markup=kb.main)

@router.message(Command('help'))
async def start_cmd(msg: Message):
    await msg.answer('Test help command')