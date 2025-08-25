from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def get_info(self):
            pass

    def __repr__(self):
            return f"{self.__class__.__name__}({self.name})"


class CreationInfoMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {args} {kwargs}")


class Product(CreationInfoMixin, BaseProduct):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description)
        self.price = price
        self.quantity = quantity

    def get_info(self):
        return f"{self.name}: {self.description}, цена: {self.price}, количество: {self.quantity}"


class Smartphone(Product):
    def __init__(self, name, description, price, quantity,
                 model=None, memory=None):
        super().__init__(name, description, price, quantity)
        self.model = model
        self.memory = memory

    def get_info(self):
        return f"{self.name} (модель: {self.model}, память: {self.memory}): {self.description}"


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity,
                 country=None):
        super().__init__(name, description, price, quantity)
        self.country = country

    def get_info(self):
        return f"{self.name} (страна происхождения: {self.country}): {self.description}"
