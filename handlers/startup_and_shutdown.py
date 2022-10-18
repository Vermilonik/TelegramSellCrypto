from datetime import datetime

from aiogram import Bot, Router

from config_reader import config

r = Router()


@r.startup()
async def on_startup(bot: Bot):
    now = datetime.now()
    now = now.strftime('%H:%M:%S')
    await bot.send_message(config.admin_id.get_secret_value(), f"бот запущен\nTime: <code>{now}</code>")


@r.shutdown()
async def shutdown(bot: Bot):
    now = datetime.now()
    now = now.strftime('%H:%M:%S')
    await bot.send_message(config.admin_id.get_secret_value(), f"бот остановлен\nTime: <code>{now}</code>")
