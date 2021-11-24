# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def division(first_number, second_number):
    try:
        print(first_number / second_number)
    except ZeroDivisionError:
        print("Деление на ноль запрещено!")


a = int(input("Введите число А "))
b = int(input("Введите число B "))
division(a, b)
