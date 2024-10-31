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
    await callback.message.answer('🎉  Добро пожаловать в мир тестовых заданий! Здесь вы найдете задачи, которые помогут вам закрепить и проверить свои знания C++.\n\n📚  Задания структурированы по темам, чтобы вы могли выбрать наиболее интересный или актуальный для вас раздел. \n\n💻  Приятный бонус: для решения задач вам не потребуется компьютер! Учитесь в любом удобном месте! \n\n🚀  Готовы к испытанию? Выберите интересующий вас раздел и номер задачи - и вперед!', reply_markup=get_test_task_keyboard())
    
@router.callback_query(F.data == 'answer_test_false', default_state)
async def test(callback: CallbackQuery):
    await callback.message.answer('Попробуй еще раз! 😉')

@router.callback_query(F.data == 'answer_test_true', default_state)
async def test(callback: CallbackQuery):
    await callback.message.edit_reply_markup()
    await callback.message.answer('Отлично! 🎉 \n\nТы справился с задачей!  👏')