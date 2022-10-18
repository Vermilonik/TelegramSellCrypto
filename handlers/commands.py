from aiogram import Router, types
from aiogram.filters.command import Command

r = Router()


@r.message(Command(commands=['start']))
async def cmd_start(m: types.Message):
    await m.answer("бот на бэта тесте!\nпривет, напиши /help , чтобы увидеть все мои команды")


@r.message(Command(commands=['help']))
async def cmd_help(m: types.Message):
    await m.answer("/start - вывод приветствия бота\n"
                   "/help - вывод этого сообщения\n"
                   "/buy <crypto name> <how much> - покупка криптовалюты\n"
                   "/source - вывод исходного кода")


@r.message(Command(commands=['source']))
async def cmd_source(m: types.Message):
    await m.answer("Исходный код бота: https://github.com/Vermilonik/TelegramSellCrypto")
