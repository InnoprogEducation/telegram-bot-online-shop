import asyncio
import logging

from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, LabeledPrice

from bot.buttons.inline import pay_button
from bot.config import config
from bot.handlers import *
from database import cart, products

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

BOT_TOKEN = config.tg_bot.token

bot = Bot(BOT_TOKEN, parse_mode="HTML")
redis = Redis(host=config.redis.host)
storage = RedisStorage(redis=redis)
dp = Dispatcher(storage=storage)

@payment_router.message(F.text == "Оплатить")
async def payment_process(message: Message):
    price = 0
    for product_id, amount in cart.get(message.chat.id).items():
        price += products[product_id - 1].price * amount
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Контакт",
        description="Приобрести",
        provider_token=config.payment.token,
        currency="RUB",
        # photo_url="https://i.ibb.co/448wWGc/avatar.png",
        # photo_width=640,
        # photo_height=640,
        # is_flexible=False,
        prices=[LabeledPrice(label="Цена", amount=round(price * 100,2))],
        start_parameter="time-machine-example",
        payload=f"ticket",
        need_name=True,
        need_email=True,
        send_email_to_provider=True,
        # provider_data={
        #     "receipt": {
        #         "items": [
        #             {
        #                 "description": "товар ",
        #                 "quantity": "1.00",
        #                 "amount": {
        #                     "value": str(price),
        #                     "currency": "RUB",
        #                 },
        #                 "vat_code": 2,
        #             }
        #         ]
        #     }
        # },
        reply_markup=await pay_button(),
    )

dp.include_routers(commands_router, callback_router, payment_router)


async def main():
    logging.info("Starting bot")
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
