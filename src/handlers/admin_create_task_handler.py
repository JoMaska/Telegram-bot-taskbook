import logging

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.admin_keyboard import get_admin_main_keyboard, get_admin_add_task_keyboard, get_admin_add_test_task_keyboard
from filters import IsAdminFilter
from keyboards.inline_keyboard import get_main_inline_keyboard

logger = logging.getLogger(__name__)

admin_router = Router()
admin_router.message.filter(IsAdminFilter())

class FSMCreateTaskAdmin(StatesGroup):
    type  = State()
    group = State()
    name = State()
    answer1 = State()
    answer2 = State()
    answer3 = State()
    answer4 = State()
    true_answer = State()
    
@admin_router.message(Command('start'))
async def start_cmd(msg: Message):
    await msg.answer('Приветствую тебя, админ!', reply_markup=get_admin_main_keyboard())
    await msg.answer('Я учебный бот Задачник С++', reply_markup=get_main_inline_keyboard())

@admin_router.message(F.text == 'Добавить задачу')
async def create_task(msg: Message, state: FSMContext):
    await msg.answer('Выбери какой тип задачи ты хочешь добавить', reply_markup=get_admin_add_task_keyboard())
    await state.set_state(FSMCreateTaskAdmin.type)

@admin_router.message(FSMCreateTaskAdmin.type, F.text == "Добавить тестовую задачу")
async def create_test_task(msg: Message, state: FSMContext):
    await state.update_data(type=msg.text.lower())
    await msg.answer('Выбери группу', reply_markup=get_admin_add_test_task_keyboard())
    await state.set_state(FSMCreateTaskAdmin.group)

@admin_router.message(FSMCreateTaskAdmin.group, F.text.in_(get_admin_add_test_task_keyboard().list_button))
async def create_test_group_task(msg: Message, state: FSMContext):
    await state.update_data(group=msg.text.lower())
    await msg.answer('Напиши название задачи', reply_markup=ReplyKeyboardRemove())
    await state.set_state(FSMCreateTaskAdmin.name)

@admin_router.message(FSMCreateTaskAdmin.name)
async def create_test_name_task(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text.lower())
    await msg.answer('Напиши ответ 1')
    await state.set_state(FSMCreateTaskAdmin.answer1)
    
@admin_router.message(FSMCreateTaskAdmin.answer1)
async def create_test_answer1_task(msg: Message, state: FSMContext):
    await state.update_data(answer1=msg.text.lower())
    await msg.answer('Напиши ответ 2')
    await state.set_state(FSMCreateTaskAdmin.answer2)
    
@admin_router.message(FSMCreateTaskAdmin.answer2)
async def create_test_answer2_task(msg: Message, state: FSMContext):
    await state.update_data(answer2=msg.text.lower())
    await msg.answer('Напиши ответ 3')
    await state.set_state(FSMCreateTaskAdmin.answer3)
    
@admin_router.message(FSMCreateTaskAdmin.answer3)
async def create_test_answer3_task(msg: Message, state: FSMContext):
    await state.update_data(answer3=msg.text.lower())
    await msg.answer('Напиши ответ 4')
    await state.set_state(FSMCreateTaskAdmin.answer4)

@admin_router.message(FSMCreateTaskAdmin.answer4)
async def create_test_answer4_task(msg: Message, state: FSMContext):
    await state.update_data(answer4=msg.text.lower())
    await msg.answer('Напиши номер правильного ответа, введенного ранее')
    await state.set_state(FSMCreateTaskAdmin.true_answer)

@admin_router.message(FSMCreateTaskAdmin.true_answer, F.text.in_(['1','2','3','4']))
async def create_test_answer4_task(msg: Message, state: FSMContext):
    await state.update_data(true_answer=msg.text)
    user_data = await state.get_data()
    
    await msg.answer(f'''Твой выбор:
Тип задачи: {user_data['type']}
Группа задачи: {user_data['group']}
Название задачи: {user_data['name']}
Первый ответ: {user_data['answer1']}
Второй ответ: {user_data['answer2']}
Третий ответ: {user_data['answer3']}
Четвертый ответ: {user_data['answer4']}
Правильный ответ указан под номером {user_data['true_answer']}
''')
    await state.clear()