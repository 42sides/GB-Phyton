from random import randrange
from itertools import count

start_list = []
end_list = []
for z in count(30):
    if len(start_list) > 20:
        break
    else:
        start_list.append(randrange(0, 1000))

z = 1
while z != len(start_list):
    if start_list[z] > start_list[z - 1]:
        end_list.append(start_list[z])
    z += 1
print(f"Первоначальный список: {start_list}")
print(f"Конечный список {end_list}")