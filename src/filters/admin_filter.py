from aiogram.filters import BaseFilter
from aiogram.types import Message

from config.config import load_config

class IsAdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        config = load_config()
        config_ids = [id for id in config.bot.admins_id.split(',')]
        return str(message.from_user.id) in config_ids