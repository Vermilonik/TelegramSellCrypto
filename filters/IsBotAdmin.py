from aiogram.filters import BaseFilter
from aiogram.types import Message

from config_reader import config


class IsBotAdmin(BaseFilter):
    async def __call__(self, m: Message):
        return str(m.from_user.id) == config.admin_id.get_secret_value()
