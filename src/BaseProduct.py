from abc import ABC, abstractmethod


class CreationInfoMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {args} {kwargs}")

class BaseProduct(CreationInfoMixin, ABC):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.name = name
        self.description = description

    @abstractmethod
    def get_info(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"



