from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Тестовые задачи', callback_data='test')],
    [InlineKeyboardButton(text= 'Практические задачи', callback_data='practice')]
    ])
