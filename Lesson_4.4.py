from random import randrange
from itertools import count

start_list = []
end_list = []
for z in count(15):
    if len(start_list) > 30:
        break
    else:
        start_list.append(randrange(0, 20))


count = 0
for num in start_list:
    for snum in start_list:
        if (num == snum):
            count += 1
    if count == 1:
        end_list.append(int(num))
    count = 0

print(f"Вывожу список сгенерированных чисел: {start_list}")
print(f"Вывожу элементы списка не имеющие повторений, в порядке следования в исходном списке: {end_list}")
