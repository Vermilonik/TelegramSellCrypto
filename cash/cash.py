from datetime import datetime

import cryptocompare
from aiogram import F
from aiogram import Router, Bot, types
from aiogram.filters.command import Command

from config_reader import config

r = Router()


@r.message(Command(commands=['buy']))
async def buy(message: types.Message, bot: Bot):
    global crypto_name
    global how_much
    crypto_name = str(message.text.split(" ")[1])
    how_much = int(message.text.split(" ")[2])
    if crypto_name != "BNB" and "USDT" and "TON":
        await message.answer(f"Написанная криптовалюта не поддерживается. введите любую криптовалюту, которая представлена ниже:\n"
                             f"1. <code>BNB</code>\n"
                             f"2. <code>USDT</code>\n"
                             f"3. <code>TON</code>\n")
    crypto_price = cryptocompare.get_price(crypto_name, currency='UAH', full=False)[crypto_name]['UAH']
    price = types.LabeledPrice(label=f"Покупка {crypto_name}", amount=how_much * crypto_price * 100)  # в копейках
    if config.payments_token.get_secret_value().split(":")[1] == 'TEST':
        await message.answer("Тестовый платеж")

    await bot.send_invoice(message.chat.id,
                           title="Покупка криптовалюты",
                           description=f"Чтобы получить криптовалюту, сначала нужно скинуть деньги. "
                                       f"Потом, если платёж пройдет удачно, автоматически скинется ",
                           provider_token=config.payments_token.get_secret_value(),
                           currency="UAH",
                           photo_url="https://cdn.igromania.ru/mnt/news/1/4/5/8/2/0/117138/903246a172030ea3_848x477.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[price],
                           start_parameter="buy-crypto",
                           payload="test-invoice-payload")


@r.pre_checkout_query(lambda query: True)
async def pre_checkout_query(p_c_q: types.PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(p_c_q.id, ok=True)


@r.message(F.content_type.in_({'successful_payment'}))
async def successful_payment(m: types.Message, bot: Bot):
    now = datetime.now()
    now = now.strftime('%H:%M:%S')
    await bot.send_message(config.admin_id.get_secret_value(),
                           f"Человек: @{m.from_user.username}\n"
                           f"Его айди: <code>{m.from_user.id}</code>\n"
                           f"Заплатил: <code>{m.successful_payment.total_amount // 100} {m.successful_payment.currency}</code>\n"
                           f"Купил {how_much}{crypto_name}\n"
                           f"Время: {now}")
