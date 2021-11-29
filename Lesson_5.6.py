import codecs

finalsub = {}

try:
    with codecs.open("lesson5_6file.txt", "r", "utf-8-sig") as file_obj:
        for line in file_obj.readlines():
            data = line.replace("(", " ").split()
            finalsub[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
except ValueError:
    print("Некорретные данные")

print(finalsub)
