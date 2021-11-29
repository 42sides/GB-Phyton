import codecs

file = codecs.open("lesson5_4file.txt", "r", "utf-8-sig")
content = file.read()
content_new = content.replace("One", "Один").replace("Two", "Два").replace("Three", "Три").replace("Four",
                                                                                                   "Четыре").split()
z = 0
h = 0
koplist = []
while z != 12:
    koplist.append(f"{content_new[z]} {content_new[z + 1]} {content_new[z + 2]}")
    z += 3
    with open("lesson5_4_2file.txt", 'a') as file_obj:
        file_obj.write(f"{koplist[h]}\n")
        h += 1
