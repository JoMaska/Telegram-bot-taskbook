import logging

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.admin_keyboard import get_admin_main_keyboard
from filters import IsAdminFilter

logger = logging.getLogger(__name__)

admin_router = Router()
admin_router.message.filter(IsAdminFilter())

@admin_router.message(Command('start'))
async def start_cmd(msg: Message):
    await msg.answer('Admin?', reply_markup=get_admin_main_keyboard())

@admin_router.message(F.text == 'Добавить задачу')
async def start_cmd(msg: Message):
    await msg.answer('Test admin create task command')

@admin_router.message(F.text == 'Удалить задачу')
async def start_cmd(msg: Message):
    await msg.answer('Test admin delete task command')