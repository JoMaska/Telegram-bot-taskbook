from aiogram.filters import BaseFilter
from aiogram.types import Message

from config.config import load_config

class IsAdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        config = load_config()
        admin_id = config.bot.admin_id
        return message.from_user.id == int(admin_id)