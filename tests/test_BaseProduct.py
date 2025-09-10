import pytest
from src.product import Product


def test_product_creation(capsys):
    # Создаем объект продукта
    product = Product("Товар1", "Описание товара", 100, 10)

    # Проверяем атрибуты
    assert product.name == "Товар1"
    assert product.description == "Описание товара"

    # Проверяем метод get_info
    info = product.get_info()
    assert info == "Product: Товар1, Description: Описание товара"

    # Проверяем вывод в консоль (создание объекта)
    captured = capsys.readouterr()
    assert "Создан объект класса Product с параметрами: ('Товар1', 'Описание товара') {}" in captured.out

    # Проверяем __repr__
    assert repr(product) == "Product(Товар1, 100, Описание товара, 10)"


if __name__ == "__main__":
   pytest.main()
