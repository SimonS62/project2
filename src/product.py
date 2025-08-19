class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.name = name
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
        if isinstance(value, (int, float)):
            numeric_value = value
        elif isinstance(value, str):
            try:
                numeric_value = float(value)
            except ValueError:
                raise TypeError("Цена должна быть числом")
        else:
            raise TypeError("Цена должна быть числом")

        if numeric_value <= 0:
            raise ValueError("Цена должна быть больше нуля")

        self.__price = numeric_value

    def __repr__(self):
        return f"Product({self.name}, {self.price}, {self.description}, {self.quantity})"

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self.price * self.quantity) + (other.price * other.quantity)


