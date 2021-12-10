class NotNumberException(Exception):

    def __init__(self, income_list):
        for z in income_list:
            print(z)


our_list = []
while True:
    try:
        number = input("Введите число: ")
        if number == "stop":
            NotNumberException(our_list)
            break
        elif not number.isdigit():
            print("Введено не число, введенная строка не учитывается, продолжите ввод")
        else:
            our_list.append(number)
    except ValueError as exception:
        NotNumberException(our_list)
