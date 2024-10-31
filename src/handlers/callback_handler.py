import logging

from aiogram import Router, F
from aiogram.types import CallbackQuery, ReplyKeyboardRemove, InlineKeyboardMarkup
from aiogram.fsm.state import default_state
from keyboards.keyboard import get_test_task_keyboard

router = Router()

logger = logging.getLogger(__name__)
    
@router.callback_query(F.data == 'test_task', default_state)
async def test(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Добро пожаловать в раздел с тестовыми заданиями! \nЗдесь вы найдёте задачи, разделённые по темам, которые помогут вам лучше понять и закрепить изученный материал. \nРешение этих задач не требует использования компьютера, поэтому вы можете заниматься в любом удобном месте. \nЧтобы начать, выберите интересующий вас раздел и номер задачи.', reply_markup=get_test_task_keyboard())
    
@router.callback_query(F.data == 'answer_test_false', default_state)
async def test(callback: CallbackQuery):
    await callback.answer('Неверно!')

@router.callback_query(F.data == 'answer_test_true', default_state)
async def test(callback: CallbackQuery):
    await callback.message.edit_reply_markup()
    await callback.message.answer('Ты выбрал правильный ответ!')