from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_inline_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='Тестовые задачи', callback_data='test_task')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)

def get_answer_test_task_inline_keyboard(buttons: list) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='Ответ 1', callback_data='answer_test_'+str(buttons[0][1]).lower())
    kb.button(text='Ответ 2', callback_data='answer_test_'+str(buttons[1][1]).lower())
    kb.button(text='Ответ 3', callback_data='answer_test_'+str(buttons[2][1]).lower())
    kb.button(text='Ответ 4', callback_data='answer_test_'+str(buttons[3][1]).lower())
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)