import pytest
from src.BaseProduct import BaseProduct, Product, Smartphone, LawnGrass


def test_cannot_instantiate_base_class():
    with pytest.raises(TypeError):
        # Попытка создать экземпляр абстрактного класса должна вызвать ошибку
        BaseProduct("Test", "desc")

def test_repr_returns_class_name_and_name():
    product = Product("TestProd", "desc", 1000.0, 5)
    repr_str = repr(product)
    assert "Product" in repr_str
    assert "TestProd" in repr_str

def test_creation_info_prints(capsys):
    # Проверяем что при создании объекта выводится сообщение
    product = Product("TestProd", "desc", 100.0, 10)
    captured = capsys.readouterr()
    assert "Создан объект класса Product" in captured.out
    assert "TestProd" in captured.out

def test_get_info_product():
    product = Product("Prod", "desc", 200.0, 3)
    info = product.get_info()
    assert "Prod:" in info
    assert "цена: 200.0" in info
    assert "количество: 3" in info

def test_get_info_smartphone():
    phone = Smartphone("iPhone", "smartphone desc", 999.99, 2,
                       model="X", memory="128GB")
    info = phone.get_info()
    assert "iPhone" in info
    assert "(модель: X" in info
    assert "память: 128GB" in info

def test_get_info_lawn_grass():
    grass = LawnGrass("Lawn", "grass desc", 15.5, 20,
                      country="USA")
    info = grass.get_info()
    assert "Lawn" in info
    assert "(страна происхождения: USA)" in info

def test_repr_inheritance_and_repr_output():
    g = LawnGrass("Lawn", "desc", 10.0, 1)
    r = repr(g)
    assert r.startswith("LawnGrass")


if __name__ == "__main__":
   pytest.main()
