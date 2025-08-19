import unittest
import pytest
from src.category import Category
from src.product import Product


class TestProductAndCategory(unittest.TestCase):
    def setUp(self):
        # Обнуляем счетчики перед каждым тестом
        Category.category_count = 0
        Category.product_count = 0

    def test_create_product(self):
        product = Product("Test Product", "Description", 100.0, 10)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Description")
        self.assertEqual(product.price, 100.0)
        self.assertEqual(product.quantity, 10)

    def test_create_category_with_products(self):
        p1 = Product("P1", "Desc1", 50.0, 5)
        p2 = Product("P2", "Desc2", 75.0, 3)
        category = Category("Test Category", "Category description", [p1, p2])

        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "Category description")
        self.assertEqual(len(category.products), 2)

        # Проверка счетчиков
        self.assertEqual(Category.category_count, 1)
        self.assertEqual(Category.product_count, 2)

    def test_category_counter_increment(self):
        p1 = Product("P1", "Desc1", 50.0, 5)
        cat1 = Category("Cat1", "Desc", [p1])

        p2 = Product("P2", "Desc2", 75.0, 3)
        cat2 = Category("Cat2", "Desc2", [p2])

        # Общее число категорий и товаров
        self.assertEqual(Category.category_count, 2)
        self.assertEqual(Category.product_count, 2)

    def test_product_counter_with_multiple_categories(self):
        p1 = Product("P1", "Desc1", 50.0, 5)
        p2 = Product("P2", "Desc2", 75.0, 3)

        cat1 = Category("Cat1", "Desc", [p1])
        cat2 = Category("Cat2", "Desc", [p2])

        # Общее число товаров должно быть суммой товаров из обеих категорий
        total_products_in_categories = len(cat1.products) + len(cat2.products)
        self.assertEqual(Category.product_count, total_products_in_categories)


class TestProduct(unittest.TestCase):

    def test_create_new_product(self):
        data = {
            'name': 'Телефон',
            'price': 15000,
            'description': 'Смартфон',
            'quantity': 10
        }
        product = Product.new_product(data)
        self.assertEqual(product.name, 'Телефон')
        self.assertEqual(product.price, 15000)
        self.assertEqual(product.description, 'Смартфон')
        self.assertEqual(product.quantity, 10)

    def test_set_positive_price(self):
        product = Product("Телефон", 1000, "Описание", 5)
        product.price = 2000
        self.assertEqual(product.price, 2000)

    def test_set_zero_price(self):
        product = Product("Телефон", 1000, "Описание", 5)
        with pytest.raises(ValueError):
            product.price = 0

    def test_set_negative_price(self):
        product = Product("Телефон", 1000, "Описание", 5)
        with pytest.raises(ValueError):
            product.price = -50


class TestProductStrAndCategoryStr(unittest.TestCase):

    def test_product_str(self):
        p = Product("Молоко", 80, "Описание продукта", 15)
        expected_str = "Молоко, 80 руб. Остаток: 15 шт."
        self.assertEqual(str(p), expected_str)

    def test_category_str(self):
        p1 = Product("Молоко", "Свежие продукты", 50.0, 10)
        p2 = Product("Хлеб", "Пекарские изделия", 30.0, 5)

        category_name = "Бакалея"

        cat = Category(category_name, "Раздел продуктов питания", [p1, p2])

        total_quantity = sum(p.quantity for p in cat.products)

        expected_str = f"{category_name}, количество продуктов: {total_quantity} шт."

        self.assertEqual(str(cat), expected_str)


def test_product_add():
    p1 = Product("Молоко", 80, "Описание продукта", "15")
    p2 = Product("Хлеб", 30, "Описание хлеба", "20")

    total_cost = p1 + p2
    expected_total = (80 * int(p1.quantity)) + (30 * int(p2.quantity))

    assert total_cost == expected_total


def test_add_with_non_product():
    p = Product("Молоко", 80, "Описание продукта", "15")
    with pytest.raises(TypeError):
        _ = p + "not a product"


# В конце файла оставьте только один вызов unittest.main()
if __name__ == '__main__':
    unittest.main()
