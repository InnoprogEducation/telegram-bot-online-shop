from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from database.product import Product



async def generate_card_keyboard(product: Product, amount: int):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="-", callback_data=f"decrease_amount:{product.id}:{amount}"
                ),
                InlineKeyboardButton(text=f"{amount}", callback_data="-"),
                InlineKeyboardButton(
                    text="+", callback_data=f"increase_amount:{product.id}:{amount}"
                ),
            ],
            [
                InlineKeyboardButton(
                    text=f"Добавить в корзину🛒 ({round(amount * product.price, 2)}р)",
                    callback_data=f"add_to_cart:{product.id}:{amount}",
                )
            ],
            [
                InlineKeyboardButton(
                    text="Закрыть карточку товара", callback_data="close_card"
                )
            ],
        ]
    )


async def start_buttons(product: Product):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть карточку товара",
                    callback_data=f"show_product_card:{product.id}",
                )
            ]
        ]
    )

async def cart_item_change(product, amount):
    return InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="Изменить", callback_data=f"edit:{product.id}:{amount}")
        ]])


async def ask_keyboard(product, amount):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Да", callback_data=f"delete_cart_item:{product.id}:{amount}:1"),
         InlineKeyboardButton(text="Нет", callback_data=f"delete_cart_item:{product.id}:{amount}:0"), ]
    ])
async def cart_item_extended_keyboard(product: Product, amount: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='-', callback_data=f'decrease_item_amount:{product.id}:{amount}'),
         InlineKeyboardButton(text=f"{amount}", callback_data='just_display'),
         InlineKeyboardButton(text="+", callback_data=f'increase_item_amount:{product.id}:{amount}')],
        [InlineKeyboardButton(text="Удалить🗑", callback_data=f'delete_item:{product.id}:{amount}'),
         InlineKeyboardButton(text="Свернуть", callback_data=f'cancel_item:{product.id}:{amount}')]
    ])

async def pay_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Приобрести билет", pay=True)]
        ]
    )

