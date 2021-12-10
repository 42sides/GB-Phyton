class Date:

    def __init__(self, str_date):
        self.__str_date = str(str_date)

    @classmethod
    def get_to_number(cls, str_date):
        get_to_list = str_date.split("-")
        int_list = []
        for x in get_to_list:
            int_list.append(int(x))
        print(f"Текущая дата: {int_list[0]} число, {int_list[1]} месяц, {int_list[2]} год")
        return Date.validation(int(int_list[0]), int(int_list[1]), int(int_list[2]))

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return "Все верно"
                else:
                    return "Год указан неверно"
            else:
                return "Месяц указан неверно"
        else:
            return "День указан неверно"

    def __str__(self):
        return f'{Date.get_to_number(self.__str_date)}'


today = Date("11 - 1 - 2001")
print(today)
print(Date.get_to_number("11 - 1 - 2001"))
print(Date.get_to_number("11 - 14 - 2001"))
print(Date.get_to_number("45 - 1 - 2001"))
print(Date.get_to_number("11 - 1 - 2027"))
