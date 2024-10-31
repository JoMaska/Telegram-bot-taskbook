import logging

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from aiogram.fsm.state import default_state
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.keyboard import get_test_task_keyboard
from keyboards.inline_keyboard import get_answer_test_task_inline_keyboard
from database.models import Task, Answer

logger = logging.getLogger(__name__)

router = Router()

class FSMShowTask(StatesGroup):
    show_task = State()
    
@router.message(F.text.in_(get_test_task_keyboard().list_button), default_state)
async def show_test_task(msg: Message, session: AsyncSession, state: FSMContext):
    result = await session.execute(select(Task.id, Task.desc).where(Task.group == msg.text))
    all_results = result.all()
    if all_results != []:
        result = ''.join(f'{id}. {desc}\n' for id, desc in all_results)
        await msg.answer(result, reply_markup=ReplyKeyboardRemove())
        await state.update_data(group=msg.text)
        await msg.answer('Отправь номер задачи, которую хочешь решить')
        await state.set_state(FSMShowTask.show_task)
    else:
        await msg.answer(f"В группе {msg.text.lower()} нет задач", reply_markup=ReplyKeyboardRemove())
    
@router.message(FSMShowTask.show_task)
async def show_test_task_with_answer(msg: Message, session: AsyncSession, state: FSMContext):
    try:
        data = int(msg.text)
        user_data = await state.get_data()
        desc = await session.scalar(select(Task.desc).where(Task.group == user_data['group'], Task.id == data))
        result_answers = await session.execute(select(Answer.desc, Answer.is_correct).where(Answer.task_id == data))
        answers = result_answers.all()
        if desc != None and answers != []:
            await state.clear()
            await msg.answer(f"{desc}\n\n1. {answers[0][0]}\n2. {answers[1][0]}\n3. {answers[2][0]}\n4. {answers[3][0]}", reply_markup=get_answer_test_task_inline_keyboard(buttons=answers))
        else:
            await msg.answer(f"Нет такой задачи", reply_markup=ReplyKeyboardRemove())
    except ValueError:
        await msg.answer('Введите число')