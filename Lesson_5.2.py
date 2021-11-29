line_count = 1
dict = {}
try:
    with open("lesson5_2file.txt") as file_obj:
        for lines in file_obj:
            b = lines.split()
            dict.update({line_count: len(b)})
            line_count += 1
except IOError:
    print("Обнаружена ошибка связанная с чтением: ")

line_count = 0

for z in dict:
    print(f"Строка {z} - количество слов в строке {dict[z]}")
    line_count += 1


print(f"В прочитанном файле всего {line_count} строк/и")
