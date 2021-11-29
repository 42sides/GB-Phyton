try:
    with open("lesson5_5file.txt", 'w') as file_obj:
        line = input("Введите строку чисел для записи в файл, разделенную пробелами (для завершения нажмите "
                     "Enter): ")
        file_obj.write(line + "\n")
except IOError:
    print("Обнаружена ошибка связанная с вводом: ")

list = []
sum = 0
try:
    with open("lesson5_5file.txt") as file_obj:
        for lines in file_obj:
            list.append(lines.replace("\n", ""))
except IOError:
    print("Обнаружена ошибка связанная с выводом: ")

list1 = list[0].split()
for h in list1:
    sum += int(h)
print(f"Сумма чисел в файле: {sum}")
