class Cart:
    def __init__(self):
        self.users_carts = {}

    def empty_cart(self, user_id: int) -> None:
        self.users_carts[user_id] = {}

    def add(self, user_id: int, product_id: int, amount: int) -> None:
        if self.users_carts.get(user_id) is None:
            self.empty_cart(user_id)
        if self.users_carts[user_id].get(product_id) is None:
            self.users_carts[user_id][product_id] = amount
        else:
            self.users_carts[user_id][product_id] += amount

    def set_value(self, user_id: int, product_id: int, value: int) -> None:
        if value == 0:
            # Удаляем товар из корзины
            self.users_carts[user_id] = {
                key: value
                for key, value in self.users_carts[user_id].items()
                if key != product_id
            }
            return
        self.users_carts[user_id][product_id] = value

    def get(self, user_id: int) -> dict:
        if self.users_carts.get(user_id) is None:
            self.empty_cart(user_id)
        return self.users_carts[user_id]


cart = Cart()
