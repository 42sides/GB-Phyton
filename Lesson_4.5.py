from functools import reduce


def function(first_element, second_element):
    return first_element + second_element


my_set = [el for el in range(100, 1001) if el % 2 == 0]

print(f"Вывожу список чисел: {my_set}")
print(f"Вывожу сумму списка чисел: {reduce(function, my_set)}")
