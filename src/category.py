from typing import List
from src.product import Product


class Category:
    category_count = 0  # Общее число категорий
    product_count = 0   # Общее число товаров во всех категориях

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products

        # Обновляем счетчики при создании нового объекта
        Category.category_count += 1
        Category.product_count += len(products)
        self.name = name
        self.description = description
        self.__products = []  # приватный список товаров

    def add_product(self, product: Product):
        self.__products.append(product)

    @property
    def products(self):
        # Возвращаем список строк с информацией о товарах
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )
