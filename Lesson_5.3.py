import codecs

line_count = 1

file = codecs.open("lesson5_3file.txt", "r", "utf-8-sig")
content = file.read()

content_new = content.split("\n")

salary = 0
print("Список сотрудников с заработной платой более 20 000 рублей:\n")
for i in content_new:
    list = i.replace('\r', '').split(" ")

    if int(float(list[1])) > 20000:
        print(list[0])
    salary += int(float(list[1]))

print(f"\nСредняя зарплата сотрудников: {salary / len(content_new)}")
