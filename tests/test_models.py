import unittest
from src.models import Product, Category


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
        # Создаем несколько категорий и проверяем счетчики
        p1 = Product("P1", "Desc1", 50.0, 5)
        cat1 = Category("Cat1", "Desc", [p1])

        p2 = Product("P2", "Desc2", 75.0, 3)
        cat2 = Category("Cat2", "Desc2", [p2])

        self.assertEqual(Category.category_count, 2)
        self.assertEqual(Category.product_count, 2)

    def test_product_counter_with_multiple_categories(self):
        p1 = Product("P1", "Desc1", 50.0, 5)
        p2 = Product("P2", "Desc2", 75.0, 3)

        cat1 = Category("Cat1", "Desc", [p1])
        cat2 = Category("Cat2", "Desc", [p2])

        # Общее число товаров должно быть суммой товаров из обеих категорий
        self.assertEqual(Category.product_count, len(cat1.products) + len(cat2.products))


if __name__ == '__main__':
    unittest.main()
