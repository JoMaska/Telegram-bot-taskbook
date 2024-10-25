from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_admin_main_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Добавить задачу')
    kb.button(text='Удалить задачу')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)