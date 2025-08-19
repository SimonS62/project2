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
        if value <= 0:
            print("Цена не должна быть нулевой или отрицательной")
        else:
            self.__price = value

    def __repr__(self):
        return f"Product({self.name}, {self.price}, {self.description}, {self.quantity})"
