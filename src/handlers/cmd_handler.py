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
    await msg.answer('👋  Приветствуем вас, будущие программисты!\n\n🚀  Задачник С++ - это проект, разработанный студентами 1 курса Московского Политеха, который поможет вам освоить язык программирования C++.\n\n📚  Здесь вы найдете разнообразные задачи, которые помогут вам:\n\n Проверить свои знания языка C++.\n Отточить практические навыки.\n Повторить необходимые темы.\n\n💪  Уже сейчас вы можете приступить к решению тестовых заданий! Выберите категорию, которая вам интересна, и приступайте к работе. \n\n🌟  Желаем вам успехов и интересных открытий в мире программирования!', reply_markup=get_main_inline_keyboard())

@router.message(IsAdminFilter(), Command('start'), default_state)
async def start_cmd(msg: Message):
    await msg.answer('Приветствую тебя, админ! 👋', reply_markup=get_admin_main_keyboard())
    await msg.answer('🚀  Задачник С++ - это проект, разработанный студентами 1 курса Московского Политеха, который поможет вам освоить язык программирования C++.\n\n📚  Здесь вы найдете разнообразные задачи, которые помогут вам:\n\n Проверить свои знания языка C++.\n Отточить практические навыки.\n Повторить необходимые темы.\n\n💪  Уже сейчас вы можете приступить к решению тестовых заданий! Выберите категорию, которая вам интересна, и приступайте к работе. \n\n🌟  Желаем вам успехов и интересных открытий в мире программирования!', reply_markup=get_main_inline_keyboard())

@router.message(Command('help'), default_state)
async def help_cmd(msg: Message):
    await msg.answer('Бот разработан на языке Python, с использованием фреймворка aiogram, ORM SQLAlchemy и базой данных SQLite.\n\nКоманда: \n\nРазработчики: @JoMaska, @Polina_Petrova\nХудожник: @doshiksha\nСоздатели контента и задач: @Scrws, @hochuokroshku\n\nПроект выложен на GitHub: https://github.com/JoMaska/Telegram-bot-taskbook')
    
@router.message(IsAdminFilter(), Command('cancel'))
async def cancel_cmd(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer('Действие отменено', reply_markup=get_admin_main_keyboard())

@router.message(~IsAdminFilter(), Command('cancel'))
async def cancel_cmd(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer('Действие отменено', reply_markup=ReplyKeyboardRemove())
