import logging
from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

logger = logging.getLogger(__name__)
    
@router.callback_query(F.data == 'test')
async def test(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('test task')
    
    
@router.callback_query(F.data == 'practice')
async def test(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('practical task')
