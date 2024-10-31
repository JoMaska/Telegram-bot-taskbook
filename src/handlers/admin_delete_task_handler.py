import logging

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from keyboards.admin_keyboard import get_admin_delete_task_keyboard, get_admin_main_keyboard
from keyboards.keyboard import get_test_task_keyboard
from filters import IsAdminFilter
from database.models import Task, Answer

logger = logging.getLogger(__name__)

admin_router = Router()
admin_router.message.filter(IsAdminFilter())

class FSMDeleteTaskAdmin(StatesGroup):
    type = State()
    group = State()
    id = State()
    finally_task = State()
    
@admin_router.message(F.text == 'Удалить задачу', default_state)
async def delete_task(msg: Message, state: FSMDeleteTaskAdmin):
    await msg.answer('Выбери тип задачи', reply_markup=get_admin_delete_task_keyboard())
    await state.set_state(FSMDeleteTaskAdmin.type)

@admin_router.message(FSMDeleteTaskAdmin.type, F.text == "Удалить тестовую задачу")
async def delete_test_task(msg: Message, state: FSMContext):
    await state.update_data(type=msg.text)
    await msg.answer('Выбери группу', reply_markup=get_test_task_keyboard())
    await state.set_state(FSMDeleteTaskAdmin.group)

@admin_router.message(FSMDeleteTaskAdmin.group, F.text.in_(get_test_task_keyboard().list_button))
async def delete_test_group_task(msg: Message, state: FSMContext, session: AsyncSession):
    result = await session.execute(select(Task.id, Task.desc).where(Task.group == msg.text))
    all_results = result.all()
    if all_results != []:
        result = ''.join(f'{id}. {desc}\n' for id, desc in all_results)
        await msg.answer(result, reply_markup=ReplyKeyboardRemove())
        await state.update_data(group=msg.text)
        await msg.answer('Отправь номер задачи для удаления')
        await state.set_state(FSMDeleteTaskAdmin.id)
    else:
        await msg.answer(f"В группе {msg.text.lower()} нет задач", reply_markup=get_admin_main_keyboard())
    
@admin_router.message(FSMDeleteTaskAdmin.id)
async def delete_test_id_task(msg: Message, state: FSMContext):
    await state.update_data(id=msg.text)
    user_data = await state.get_data()
    await msg.answer(f"Твой выбор:\nТип задачи: {user_data['type']}\nГруппа задачи: {user_data['group']}\nНомер задачи: {user_data['id']}\nЕсли все верно, отправь 'Да', иначе отправь 'Нет'")
    await state.set_state(FSMDeleteTaskAdmin.finally_task)
    
@admin_router.message(FSMDeleteTaskAdmin.finally_task, F.text.lower() == 'да')
async def delete_test_finally_task_yes(msg: Message, state: FSMContext, session: AsyncSession):
    try:
        user_data = await state.get_data()
        await state.clear()
        await session.execute(delete(Task).where(Task.id == int(user_data['id'])))
        await session.execute(delete(Answer).where(Answer.task_id == int(user_data['id'])))
        await session.commit()
        await msg.answer('Задача была удалена', reply_markup=get_admin_main_keyboard())
    except ValueError:
        await msg.answer('Неправильный номер задачи')
        await msg.answer('Действие отменено', reply_markup=get_admin_main_keyboard())
    await state.clear()

@admin_router.message(FSMDeleteTaskAdmin.finally_task, F.text.lower() == 'нет')
async def delete_test_finally_task_no(msg: Message, state: FSMContext):
    await msg.answer('Действие отменено', reply_markup=get_admin_main_keyboard())
    await state.clear()