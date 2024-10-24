import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.inline_keyboards import get_main_inline_keyboard

logger = logging.getLogger(__name__)

router = Router()

@router.message(Command('start'))
async def start_cmd(msg: Message):
    await msg.answer('Приветствую тебя! Я учебный бот Задачник С++ - проект учеников 1 курса Московского Политеха. \nВы сможете решать различного рода задачи на знание языка, практиковать свои умения и повторить необходимые вам темы. \nУже сейчас вы можете приступить к выполнению заданий. \nВам предложены тестовые и практические задания. \nВыбирайте категорию и приступайте к работе!  Всем удачи!', reply_markup=get_main_inline_keyboard())

@router.message(Command('help'))
async def start_cmd(msg: Message):
    await msg.answer('Test help command')