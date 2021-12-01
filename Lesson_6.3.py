class Worker:
    name = str
    surname = str
    position = str
    _income = dict

    def __init__(self, name, surname, position):
        _company_dict = {"Олег Иванов": {"wage": 100000, "bonus": 50000},
                         "Алина Петрова": {"wage": 30000, "bonus": 20000}}
        self.name = name
        self.surname = surname
        self.position = position
        # self._income = sum(Worker.income_dict.values())
        self._income = sum(_company_dict.get(f"{self.name} {self.surname}").values())

    def person_info(self):
        return f"Меня зовут {self.name}, моя фамилия {self.surname}. Я работа на должности {self.position}, " \
               f"с доходом {self._income} рублей"


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self.__dict__.values())


person_1 = Position("Олег", "Иванов", "Аудитор")
person_2 = Position("Алина", "Петрова", "Менеджер")

print(person_1.person_info())
print(person_2.person_info())
