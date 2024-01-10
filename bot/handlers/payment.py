from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery

from bot.buttons.inline import pay_button
from bot.config import config
from database import cart, products

from aiogram.types import Message

payment_router = Router()


@payment_router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)


@payment_router.message(
    lambda message: message.content_type
                    in {ContentType.SUCCESSFUL_PAYMENT}
)
async def got_payment(message: Message):
    await message.answer("Оплата прошла успешно")
