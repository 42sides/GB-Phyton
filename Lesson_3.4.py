# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.

positive_number_x = float(input("Введите положительное число "))
negative_number_y = int(input("Введите отрицательное число "))


def my_func(x, y):
    z = x ** y
    print(f"Ответ с помощью оператора ** {z}")

    count = 0
    answer = 1/x
    while count < abs(y)-1:
        answer *= 1/x
        count += 1
    print(f"Ответ с помощью цикла {answer}")


my_func(positive_number_x, negative_number_y)
