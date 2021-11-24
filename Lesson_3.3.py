# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.

def my_func(first_number, second_number, third_number):
    numbers_list = [first_number, second_number, third_number]
    numbers_list.sort()
    return numbers_list[1] + numbers_list[2]


number_one = 40
number_two = 20
number_three = 50

print(my_func(number_one, number_two, number_three))
