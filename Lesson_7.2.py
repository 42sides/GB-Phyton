from abc import ABC, abstractmethod

list = []


class Weather(ABC):

    @abstractmethod
    def calculate(self):
        pass


class Coat(Weather):
    _v = int
    calculates = int

    def __init__(self, v):
        self.v = v

    @property
    def calculate(self):
        consumption = self.v / 6.5 + 0.5
        list.append(consumption)
        return f"Расходы на пальто: {consumption}"


class Costume(Weather):
    _h = int
    calculates = int

    def __init__(self, h):
        self.h = h

    @property
    def calculate(self):
        consumption = 2 * self.h + 0.3
        list.append(consumption)
        return f"Расходы на костюм: {consumption}"


coat = Coat(5)
costume = Costume(10)
print(coat.calculate)
print(costume.calculate)

print(f"Сумма всех расходов на одежду: {sum(list)}")
