import logging

from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

logger = logging.getLogger(__name__)
    
@router.callback_query(F.data == 'test_task')
async def test(callback: CallbackQuery):
    await callback.message.answer('Добро пожаловать в раздел с тестовыми заданиями! \nЗдесь вы найдёте задачи, разделённые по темам, которые помогут вам лучше понять и закрепить изученный материал. \nРешение этих задач не требует использования компьютера, поэтому вы можете заниматься в любом удобном месте. \nЧтобы начать, выберите интересующий вас раздел и номер задачи.')
    
@router.callback_query(F.data == 'practical_task')
async def test(callback: CallbackQuery):
    await callback.message.answer('Добро пожаловать в раздел с практическими заданиями! \nЗдесь вас ждут задачи, которые помогут улучшить навыки программирования. \nЧтобы решить эти задачи, вам необходимо написать программу и ввести результат её выполнения. \nЕсли результат неправильный, не расстраивайтесь: вы сможете ознакомиться с нашим решением и разобрать его. \nВыберите номер задачи, чтобы начать.')
