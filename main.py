import asyncio
import logging

from aiogram import Bot, Dispatcher

from cash import cash
from config_reader import config
from handlers import startup_and_shutdown, commands


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(config.token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(cash.r)
    dp.include_router(startup_and_shutdown.r)
    dp.include_router(commands.r)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
