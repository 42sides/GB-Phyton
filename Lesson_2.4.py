userString = input("Введите строку ")
tempWordsList = []
worldList = []
tempString = ""
count = 0
for o in userString:
    if o != " ":
        tempString += o
    else:
        tempWordsList.append(tempString)
        tempString = ""
tempWordsList.append(tempString)
tempString = ""

for b in tempWordsList:
    if len(b) > 10:
        while count != 10:
            tempString += b[count]
            count += 1
        worldList.append(tempString)
        tempString = ""
        count = 0
    else:
        worldList.append(b)

for k in worldList:
    print(k)
