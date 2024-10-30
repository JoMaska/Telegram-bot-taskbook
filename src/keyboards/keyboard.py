from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_test_task_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Типы данных и функции')
    kb.button(text='Условные операторы и циклы')
    kb.button(text='Массивы')
    kb.button(text='Структуры и классы')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, list_button=['Типы данных и функции','Условные операторы и циклы','Массивы','Структуры и классы'])
