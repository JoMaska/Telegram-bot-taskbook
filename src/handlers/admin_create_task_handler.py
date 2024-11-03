import logging

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from keyboards.admin_keyboard import get_admin_create_task_keyboard, get_admin_main_keyboard
from keyboards.keyboard import get_test_task_keyboard
from filters import IsAdminFilter
from database.models import Task, Answer

logger = logging.getLogger(__name__)

admin_router = Router()
admin_router.message.filter(IsAdminFilter())

class FSMCreateTaskAdmin(StatesGroup):
    type = State()
    group = State()
    name = State()
    desc = State()
    answer1 = State()
    answer2 = State()
    answer3 = State()
    answer4 = State()
    true_answer = State()
    finally_task = State()
    
@admin_router.message(F.text == 'Добавить задачу')
async def create_task(msg: Message, state: FSMCreateTaskAdmin):
    await msg.answer('Выбери тип задачи', reply_markup=get_admin_create_task_keyboard())
    await state.set_state(FSMCreateTaskAdmin.type)

@admin_router.message(FSMCreateTaskAdmin.type, F.text == "Добавить тестовую задачу")
async def create_test_task(msg: Message, state: FSMContext):
    await state.update_data(type=msg.text)
    await msg.answer('Выбери группу', reply_markup=get_test_task_keyboard())
    await state.set_state(FSMCreateTaskAdmin.group)

@admin_router.message(FSMCreateTaskAdmin.group, F.text.in_(get_test_task_keyboard().list_button))
async def create_test_group_task(msg: Message, state: FSMContext):
    await state.update_data(group=msg.text)
    await msg.answer('Напиши название задачи', reply_markup=ReplyKeyboardRemove())
    await state.set_state(FSMCreateTaskAdmin.name)

@admin_router.message(FSMCreateTaskAdmin.name)
async def create_test_name_task(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer('Напиши описание к задаче, если оно есть, иначе отправь "None"')
    await state.set_state(FSMCreateTaskAdmin.desc)
    
@admin_router.message(FSMCreateTaskAdmin.desc)
async def create_test_name_task(msg: Message, state: FSMContext):
    if msg.text.lower() == 'none':
        await state.update_data(desc='')
    else:
        await state.update_data(desc=msg.text)
    await msg.answer('Напиши ответ 1')
    await state.set_state(FSMCreateTaskAdmin.answer1)
    
@admin_router.message(FSMCreateTaskAdmin.answer1)
async def create_test_answer1_task(msg: Message, state: FSMContext):
    await state.update_data(answer1=msg.text)
    await msg.answer('Напиши ответ 2')
    await state.set_state(FSMCreateTaskAdmin.answer2)
    
@admin_router.message(FSMCreateTaskAdmin.answer2)
async def create_test_answer2_task(msg: Message, state: FSMContext):
    await state.update_data(answer2=msg.text)
    await msg.answer('Напиши ответ 3')
    await state.set_state(FSMCreateTaskAdmin.answer3)
    
@admin_router.message(FSMCreateTaskAdmin.answer3)
async def create_test_answer3_task(msg: Message, state: FSMContext):
    await state.update_data(answer3=msg.text)
    await msg.answer('Напиши ответ 4')
    await state.set_state(FSMCreateTaskAdmin.answer4)

@admin_router.message(FSMCreateTaskAdmin.answer4)
async def create_test_answer4_task(msg: Message, state: FSMContext):
    await state.update_data(answer4=msg.text)
    await msg.answer('Напиши номер правильного ответа, введенного ранее')
    await state.set_state(FSMCreateTaskAdmin.true_answer)

@admin_router.message(FSMCreateTaskAdmin.true_answer, F.text.in_(['1','2','3','4']))
async def create_test_true_answer_task(msg: Message, state: FSMContext):
    await state.update_data(true_answer=msg.text)
    user_data = await state.get_data()
    await msg.answer(f"Твой выбор:\nТип задачи: {user_data['type']}\nГруппа задачи: {user_data['group']}\nНазвание задачи: {user_data['name']}\nОписание задачи: {user_data['desc']}\nПервый ответ: {user_data['answer1']}\nВторой ответ: {user_data['answer2']}\nТретий ответ: {user_data['answer3']}\nЧетвертый ответ: {user_data['answer4']}\nПравильный ответ указан под номером {user_data['true_answer']}\nЕсли все верно, отправь 'Да', иначе отправь 'Нет'")
    await state.set_state(FSMCreateTaskAdmin.finally_task)

@admin_router.message(FSMCreateTaskAdmin.true_answer)
async def create_test_true_answer_task_echo(msg: Message):
    await msg.answer('Напиши номер правильного ответа, введенного ранее')

@admin_router.message(FSMCreateTaskAdmin.finally_task, F.text.lower() == 'да')
async def create_test_finally_task_yes(msg: Message, state: FSMContext, session: AsyncSession):
    user_data = await state.get_data()
    answers = [x[-1] == user_data['true_answer'] for x in user_data if 'answer' in x][:4]
    data = Task(
        group=user_data['group'],
        name=user_data['name'],
        desc=user_data['desc'],
        answers=[Answer(desc=user_data['answer1'], is_correct=answers[0]),
                 Answer(desc=user_data['answer2'], is_correct=answers[1]),
                 Answer(desc=user_data['answer3'], is_correct=answers[2]),
                 Answer(desc=user_data['answer4'], is_correct=answers[3])]
    )
    await session.merge(data)
    await session.commit()
    await msg.answer('Данные были добавлены успешно!', reply_markup=get_admin_main_keyboard())
    await state.clear()

@admin_router.message(FSMCreateTaskAdmin.finally_task, F.text.lower() == 'нет')
async def create_test_finally_task_no(msg: Message, state: FSMContext):
    await msg.answer('Действие отменено', reply_markup=ReplyKeyboardRemove())
    await state.clear()