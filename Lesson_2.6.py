list = []
name = []
price = []
cnt = []
measure = []

z = None
while z != 1:
    s1 = input("Введите номер товара ")
    if s1 != "":
        s2 = input("Введите название товара ")
        s3 = int(input("Введите цену товара "))
        s4 = int(input("Введите количество товара "))
        s5 = input("Единица измерения ")

        kort = (s1, {"название": s2,
                     "цена": s3,
                     "количество": s4,
                     "ед": s5})
        list.append(kort)
        name.append(s2)
        price.append(s3)
        cnt.append(s4)
        measure.append(s5)
    else:
        z = 1

dict = {"название": set(name),
        "цена": set(price),
        "количество": set(cnt),
        "ед": set(measure)}

for o in list:
    print(o)

print(dict)