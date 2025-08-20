class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.quantity = quantity
        self.__price = price  # приватный атрибут цены
        self.description = description
        self.quantity = quantity

    @classmethod
    def new_product(cls, data: dict):
        return cls(
            name=data.get('name'),
            price=data.get('price'),
            description=data.get('description'),
            quantity=data.get('quantity')
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        # Проверка типа и преобразование
        if isinstance(value, (int, float)):
            numeric_value = value
        elif isinstance(value, str):
            try:
                numeric_value = float(value)
            except ValueError:
                raise TypeError("Цена должна быть числом")
        else:
            raise TypeError("Цена должна быть числом")

        # Проверка на положительность
        if numeric_value <= 0:
            raise ValueError("Цена должна быть больше нуля")

        # Установка значения
        self.__price = numeric_value

    def __repr__(self):
        return f"Product({self.name}, {self.price}, {self.description}, {self.quantity})"

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.price * self.quantity) + (other.price * other.quantity)

class Smartphone(Product):
    def __init__(self, name, price, description, quantity,
                 efficiency, model, memory, color):
        super().__init__(name, price, description, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if not isinstance(other, Smartphone):
            raise TypeError("Можно складывать только смартфоны")
        new_quantity = self.quantity + other.quantity
        # Создаем новый объект Smartphone с объединенными свойствами
        return Smartphone(
            name=self.name,
            price=self.price,
            description=self.description,
            quantity=new_quantity,
            efficiency=self.efficiency,
            model=self.model,
            memory=self.memory,
            color=self.color
        )

class LawnGrass(Product):
    def __init__(self, name, price, description, quantity,
                 country, germination_period, color):
        super().__init__(name, price, description, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if not isinstance(other, LawnGrass):
            return NotImplemented
        new_quantity = self.quantity + other.quantity
        return LawnGrass(
            name=self.name,
            price=self.price,
            description=self.description,
            quantity=new_quantity,
            country=self.country,
            germination_period=self.germination_period,
            color=self.color
        )
