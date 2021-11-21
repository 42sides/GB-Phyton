newList1 = []
while True:
    x = input("Введите значение")
    if x == "":
        break
    else:
        newList1.append(x)

newList2 = []
count = int(0)

while len(newList1) > count:
    newList2.append(newList1[count + 1])
    newList2.append(newList1[count])
    count += 2
    if len(newList1) % 2 != 0 and count + 1 == len(newList1):
        newList2.append(newList1[len(newList1) - 1])
        break

print(newList2)