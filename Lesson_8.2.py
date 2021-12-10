class NullException(Exception):
    first_number = int
    second_number = int

    def __init__(self, a, b):
        self.first_number = a
        self.second_number = b

    def __str__(self):
        print(f"Деление на ноль запрещено, делимое {self.first_number}, делитель {self.second_number}")


class Money:
    a = int
    b = int

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def operation(self):
        if self.b == 0:
            raise NullException(int(self.a), int(self.b))
        else:
            print(f"Результат целочисленного деления {self.a // self.b}")


money = Money(int(input("Число 1 ")), int(input("Число 2 ")))

try:
    Money.operation(money)
except NullException as exception:
    print(f"Введено недопустимое число: {exception.second_number}")
