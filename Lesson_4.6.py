from itertools import count
from random import randrange
from itertools import cycle

first_list = []
start = int(input("Введите число, с которого Вы хотели бы начать первую генерацию: "))
end = int(input("Введите число, до которого Вы хотели бы провести первую генерацию: "))
for num in count(start):
    if num > end:
        break
    else:
        first_list.append(num)

print(f"Первая генерация была произведена, был получен следующий список чисел: {first_list}")

second_list = []
for z in count(30):
    if len(second_list) > 20:
        break
    else:
        second_list.append(randrange(0, 1000))

third_list = []

for el in cycle(second_list):
    if len(second_list) == len(third_list):
        break
    third_list.append(el)

print(f"Генератор создающий некий список: {second_list}")
print(f"Итератор, повторяющий элементы ранее сгенерированного списка {third_list}")
