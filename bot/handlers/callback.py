from aiogram import Router
from aiogram.types import CallbackQuery, FSInputFile

from bot.buttons.inline import generate_card_keyboard, ask_keyboard, cart_item_extended_keyboard, cart_item_change
from bot.message_text.text import (
    CARD_TEXT,
    IMPOSSIBLE_REDUCE_QUANTITY,
    PRODUCT_SUCCESSFULLY_ADDED, cart_item_text,
)
from database import products, cart

callback_router = Router()


@callback_router.callback_query(lambda query: "show_product_card" in query.data)
async def show_product_card(query: CallbackQuery):
    product_id = int(query.data.split(":")[1])
    product = products[product_id - 1]
    default_amount = 1

    await query.message.answer_photo(
        photo=FSInputFile(product.photo),
        caption=CARD_TEXT.format(product.name, product.description, product.price),
        reply_markup=await generate_card_keyboard(
            product=product, amount=default_amount
        ),
    )


@callback_router.callback_query(lambda query: "close_card" == query.data)
async def close_card(query: CallbackQuery):
    await query.message.delete()


@callback_router.callback_query(lambda query: "decrease_amount" in query.data)
async def decrease_amount(query: CallbackQuery):
    product_id = int(query.data.split(":")[1])
    previous_amount = int(query.data.split(":")[2])
    if previous_amount == 1:
        await query.answer(IMPOSSIBLE_REDUCE_QUANTITY)
        return
    product = products[product_id - 1]

    await query.message.edit_reply_markup(
        reply_markup=await generate_card_keyboard(
            product=product, amount=previous_amount - 1
        )
    )


@callback_router.callback_query(lambda query: "increase_amount" in query.data)
async def increase_amount(query: CallbackQuery):
    product_id = int(query.data.split(":")[1])
    previous_amount = int(query.data.split(":")[2])
    product = products[product_id - 1]

    await query.message.edit_reply_markup(
        reply_markup=await generate_card_keyboard(
            product=product, amount=previous_amount + 1
        )
    )


@callback_router.callback_query(lambda query: "add_to_cart" in query.data)
async def add_to_cart(query: CallbackQuery):
    user_id = query.message.chat.id
    product_id = int(query.data.split(":")[1])
    amount = int(query.data.split(":")[2])
    cart.add(user_id=user_id, product_id=product_id, amount=amount)
    await query.answer(PRODUCT_SUCCESSFULLY_ADDED)
    await close_card(query)


@callback_router.callback_query(lambda query: "edit" in query.data)
async def show_extra_keyboard(query: CallbackQuery):
    product_id = int(query.data.split(':')[1])
    product = products[product_id - 1]
    amount = int(query.data.split(':')[2])
    cart_extended_keyboard = await cart_item_extended_keyboard(product=product, amount=amount)
    await query.message.edit_reply_markup(reply_markup=cart_extended_keyboard)


@callback_router.callback_query(lambda query: "delete_item" in query.data)
async def delete_item(query: CallbackQuery):
    product_id = int(query.data.split(':')[1])
    amount = int(query.data.split(':')[2])
    product = products[product_id - 1]

    await query.message.edit_text(text="Вы уверены что хотите удалить это из корзины?",
                                  reply_markup=await ask_keyboard(product, amount))


@callback_router.callback_query(lambda query: "delete_cart_item" in query.data)
async def delete_item_answer(query: CallbackQuery):
    product_id = int(query.data.split(':')[1])
    amount = int(query.data.split(':')[2])
    delete = int(query.data.split(':')[3])
    product = products[product_id - 1]
    if not delete:
        await query.message.edit_text(text=await cart_item_text(product, amount),
                                      reply_markup=await cart_item_extended_keyboard(product, amount))
    else:
        cart.set_value(query.message.chat.id, product.id, 0)
        await query.message.edit_text("Товар успешно удален из корзины!")


@callback_router.callback_query(lambda query: "decrease_item_amount" in query.data)
async def decrease_item_amount(query: CallbackQuery):
    product_id = int(query.data.split(':')[1])
    product = products[product_id - 1]
    amount = int(query.data.split(':')[2])
    if amount == 1:
        await delete_item(query)
        return
    cart.set_value(query.message.chat.id, product.id, amount - 1)
    await query.message.edit_text(text=await cart_item_text(product, amount - 1),
                                  reply_markup=await cart_item_extended_keyboard(product, amount - 1))


@callback_router.callback_query(lambda query: "increase_item_amount" in query.data)
async def decrease_item_amount(query: CallbackQuery):
    product_id = int(query.data.split(':')[1])
    product = products[product_id - 1]
    amount = int(query.data.split(':')[2])
    cart.set_value(query.message.chat.id, product.id, amount + 1)
    await query.message.edit_text(text=await cart_item_text(product, amount + 1),
                                  reply_markup=await cart_item_extended_keyboard(product, amount + 1))


@callback_router.callback_query(lambda query: 'cancel_item' in query.data)
async def hide_extend_keyboard(query: CallbackQuery):
    product_id = int(query.data.split(':')[1])
    product = products[product_id - 1]
    amount = int(query.data.split(':')[2])
    await query.message.edit_reply_markup(reply_markup=await cart_item_change(product, amount))

