try:
    with open("lesson5_1file.txt", 'w') as file_obj:
        while True:
            line = input("Введите строку для записи в файл: ")
            if line != "":
                file_obj.write(line + "\n")
            else:
                break
except IOError:
    print("Обнаружена ошибка связанная с вводом: ")

try:
    with open("lesson5_1file.txt") as file_obj:
        print("\n" + "Печатаем вывод строк из файла!" + "\n")
        for lines in file_obj:
            print(lines.replace("\n", ""))
except IOError:
    print("Обнаружена ошибка связанная с выводом: ")
