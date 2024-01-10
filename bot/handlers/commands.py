from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.buttons.inline import start_buttons, cart_item_change
from bot.buttons.keyboard import get_card_table
from bot.message_text.text import LIST_ITEMS, cart_item_text
from database import products, cart

commands_router = Router()


@commands_router.message(Command(commands=["list", "start"]))
async def show_product_list(message: Message):
    await message.answer(LIST_ITEMS)
    for product in products:
        await message.answer(product.name, reply_markup=await start_buttons(product))


@commands_router.message(Command(commands=["cart"]))
async def show_cart(message: Message):
    user_id = message.chat.id
    user_cart = cart.get(user_id=user_id)
    if len(user_cart.keys()) == 0:
        await message.answer("Ваша корзина пустая!")
        return
    cart_keyboard = await get_card_table()
    await message.answer("Ваша корзина:", reply_markup=cart_keyboard)

    for product_id, amount in user_cart.items():
        product = products[product_id - 1]
        item_text = await cart_item_text(product=product, amount=amount)

        await message.answer(text=item_text, reply_markup=await cart_item_change(product, amount))


@commands_router.message(Command(commands=["empty_cart"]))
async def empty_cart(message: Message):
    user_id = message.chat.id
    for k, v in cart.get(user_id).items():
        cart.set_value(user_id, k, 0)
    await message.answer("Корзина успешно очищена!")
