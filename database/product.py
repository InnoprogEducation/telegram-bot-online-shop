# Класс для описания товаров в системе
class Product:
    product_counter = 1

    def __init__(self, *, name, description, price, photo):
        self.id = Product.product_counter  # Id товара (автоматическое выделение id)
        Product.product_counter += 1
        self.name = name  # Название товара
        self.description = description  # Описание товара
        self.price = price  # Цена товара
        self.photo = photo  # Путь для фотографии товара


products = [
    Product(
        name="Футбольный мяч",
        description="Прочный мяч для игры в футбол",
        price=25.50,
        photo="database/images/football.jpg",
    ),
    Product(
        name="Баскетбольный мяч",
        description="Официальный баскетбольный мяч для игры",
        price=29.99,
        photo="database/images/basketball.jpg",
    ),
    Product(
        name="Теннисная ракетка",
        description="Профессиональная ракетка для тенниса",
        price=55.00,
        photo="database/images/tenis.jpg",
    ),
    Product(
        name="Беговые кроссовки",
        description="Удобные кроссовки для бега",
        price=79.99,
        photo="database/images/trainers.jpg",
    ),
    Product(
        name="Боксерские перчатки",
        description="Тренировочные перчатки для бокса",
        price=34.99,
        photo="database/images/boxing_gloves.jpg",
    ),
    Product(
        name="Велосипед",
        description="Городской велосипед с амортизацией",
        price=199.99,
        photo="database/images/bicycle.jpg",
    ),
    Product(
        name="Беговая дорожка",
        description="Электрическая беговая дорожка для дома",
        price=599.99,
        photo="database/images/treadmill.jpg",
    ),
    Product(
        name="Йога мат",
        description="Профессиональный йога мат для практики",
        price=45.00,
        photo="database/images/yoga_mat.jpg",
    ),
    Product(
        name="Баскетбольное кольцо",
        description="Металлическое кольцо для баскетбола",
        price=79.99,
        photo="database/images/basketbal_ring.jpg",
    ),
    Product(
        name="Скакалка",
        description="Прочная скакалка для спортивных тренировок",
        price=9.99,
        photo="database/images/jump_rope.jpg",
    ),
]