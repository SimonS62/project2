from abc import ABC, abstractmethod


class CreationInfoMixin:
    def __init__(self, *args, **kwargs):
        # Не вызываем super().__init__() чтобы избежать ошибки
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {args} {kwargs}")

class BaseProduct(CreationInfoMixin, ABC):
    def __init__(self, name, description):
        super().__init__(name, description)  # Вызов super().__init__() для цепочки
        self.name = name
        self.description = description

    @abstractmethod
    def get_info(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"


