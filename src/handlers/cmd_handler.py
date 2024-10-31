import logging

from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from keyboards.admin_keyboard import get_admin_main_keyboard
from keyboards.inline_keyboard import get_main_inline_keyboard
from filters import IsAdminFilter

logger = logging.getLogger(__name__)

router = Router()

@router.message(~IsAdminFilter(), Command('start'), default_state)
async def start_cmd(msg: Message):
    await msg.answer('Приветствую тебя')
    await msg.answer('Я учебный бот Задачник С++ - проект учеников 1 курса Московского Политеха. \nВы сможете решать различного рода задачи на знание языка, практиковать свои умения и повторять необходимые вам темы. \nУже сейчас вы можете приступить к выполнению заданий. \nВам предложены тестовые задания. \nВыбирайте категорию и приступайте к работе!\nВсем удачи!', reply_markup=get_main_inline_keyboard())

@router.message(IsAdminFilter(), Command('start'), default_state)
async def start_cmd(msg: Message):
    await msg.answer('Приветствую тебя, админ!', reply_markup=get_admin_main_keyboard())
    await msg.answer('Я учебный бот Задачник С++ - проект учеников 1 курса Московского Политеха. \nВы сможете решать различного рода задачи на знание языка, практиковать свои умения и повторять необходимые вам темы. \nУже сейчас вы можете приступить к выполнению заданий. \nВам предложены тестовые задания. \nВыбирайте категорию и приступайте к работе!\nВсем удачи!', reply_markup=get_main_inline_keyboard())

@router.message(Command('help'), default_state)
async def help_cmd(msg: Message):
    await msg.answer('Разработчики - @JoMaska, @Polina_Petrova\n\nХудожник - @doshiksha\n\nСоздатели контента и задач - @Scrws, @hochuokroshku\n\nGithub - https://github.com/JoMaska/Telegram-bot-taskbook')

@router.message(IsAdminFilter(), Command('cancel'))
async def cancel_cmd(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer('Действие отменено', reply_markup=get_admin_main_keyboard())

@router.message(~IsAdminFilter(), Command('cancel'))
async def cancel_cmd(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer('Действие отменено', reply_markup=ReplyKeyboardRemove())
