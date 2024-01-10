from database.product import Product

LIST_ITEMS = "Вот список товаров магазина:"
CARD_TEXT = """Название: {}\n
Описание: {}\n
Цена: {}р\n
"""
IMPOSSIBLE_REDUCE_QUANTITY = "Невозможно уменьшить количество товара!"
PRODUCT_SUCCESSFULLY_ADDED = "Товар успешно добавлен в корзину!"

async def cart_item_text(product: Product, amount: int):
    return f"<b>{product.name}</b> : <i>{amount}шт</i> | {round(product.price * amount, 2)}р"
