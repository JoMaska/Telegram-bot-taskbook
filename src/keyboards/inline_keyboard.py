from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_inline_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='Тестовые задачи', callback_data='test_task')
    kb.button(text='Практические задачи', callback_data='practical_task')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
