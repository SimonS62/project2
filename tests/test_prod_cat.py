import unittest
import pytest
from src.category import Category
from src.product import Product
from src.product import Smartphone, LawnGrass


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


class TestSmartphonesStrAndLawnGrassStr(unittest.TestCase):

    def test_add_same_type_smartphones(self):
        s1 = Smartphone("ModelX", 500.0, "desc", 3,
                        efficiency="High", model="X", memory="64GB", color="Black")
        s2 = Smartphone("ModelX", 500.0, "desc", 2,
                        efficiency="High", model="X", memory="64GB", color="Black")

        result = s1 + s2

        assert isinstance(result, Smartphone)
        assert result.quantity == 5

    def test_add_same_type_grass(self):
        g1 = LawnGrass("SeedA", 10.0, "desc", 20,
                       country="Canada", germination_period=14, color="Green")
        g2 = LawnGrass("SeedA", 10.0, "desc", 30,
                       country="Canada", germination_period=14, color="Green")

        result = g1 + g2

        assert isinstance(result, LawnGrass)
        assert result.quantity == 50

    def test_add_different_types_raises(self):
        s1 = Smartphone("ModelY", 600.0, "desc", 4,
                        efficiency="Medium", model="Y", memory="128GB", color="White")
        g1 = LawnGrass("SeedB", 15.0, "desc", 10,
                       country="USA", germination_period=14, color="Green")

        with pytest.raises(TypeError):
            _ = s1 + g1


if __name__ == '__main__':
    unittest.main()
