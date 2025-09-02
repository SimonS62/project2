from src.product import Product


class Category:
    category_count = 0  # Общее число категорий
    product_count = 0   # Общее число товаров во всех категориях

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        # Обновляем счетчики при создании нового объекта
        Category.category_count += 1
        Category.product_count += len(products)
        self.name = name
        self.description = description
        self.__products = []  # приватный список товаров

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты типа Product или его подклассы")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        # Возвращаем список строк с информацией о товарах
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    @products.setter
    def products(self, value):
            if not isinstance(value, list):
                raise TypeError("products должно быть списком")
            self.__products = value

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class CategoryIterator:
    def __init__(self, category):
        self._category = category
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._category.products):
            result = self._category.products[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration()

    def __iter__(self):
        return CategoryIterator(self)
