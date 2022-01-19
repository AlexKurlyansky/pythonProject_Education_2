from abc import ABC, abstractmethod


class Textil(ABC):
    def __init__(self, param):
        self._param = param

    @abstractmethod
    def get_calculation(self):
        pass

class Coat(Textil):
    def __init__(self, param):
        super().__init__(param)

    @property
    def get_calculation(self):
        return round(self._param / 6.5 + 0.5, 2)

class Jacket(Textil):
    def __init__(self, param):
        super().__init__(param)

    @property
    def get_calculation(self):
        return round(self._param * 2 + 0.3, 2)


coat = Coat(50)
jacket = Jacket(1.70)
print(f"Расчет ткани для производства пальто: {coat.get_calculation}")
print(f"Расчет ткани для производства костюма: {jacket.get_calculation}")
print(f"Общий расход ткани для производства пальто и костюма: {coat.get_calculation + jacket.get_calculation}")
