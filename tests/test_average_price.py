import pytest
from src.category import Category
from src.product import Product


def test_product_zero_quantity_raises():
    with pytest.raises(ValueError) as excinfo:
        Product("Test", "Desc", 100.0, 0)
    assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен"

def test_average_price_with_products():
    p1 = Product("P1", "Desc1", 50.0, 5)
    p2 = Product("P2", "Desc2", 150.0, 2)
    category = Category("Cat", "Desc", [p1, p2])
    assert category.average_price() == (50.0 + 150.0) / 2

def test_average_price_no_products():
    empty_category = Category("Empty", "No products")
    assert empty_category.average_price() == 0
