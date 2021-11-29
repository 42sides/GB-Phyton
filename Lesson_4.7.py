from itertools import count


def generation(number):
    for el in range(1, number + 1, 1):
        yield el


user_number = int(input("Введите число для вычисления факториала: "))
g = generation(user_number)
print(f"Полученный генератор с помощью функции yield: {g}")
factorial = 1
for element in g:
    factorial *= element
print(f"Факториал из введенного числа: {factorial}")
