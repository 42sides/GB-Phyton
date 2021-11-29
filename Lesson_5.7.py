import json
import codecs

profit = {}
avg_profit = {}
prof = 0
prof_aver = 0
i = 0
with codecs.open("lesson5_7file.txt", "r", "utf-8-sig") as file_obj:
    for line in file_obj:
        name, firm, income, lost = line.split()
        profit[name] = int(income) - int(lost)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f"Размер средней прибыли компаний - {prof_aver:}")
    else:
        print("Все компании убыточны")
    avg_profit = {"средняя прибыль": round(prof_aver)}
    profit.update(avg_profit)
    print(f"Прибыль каждой компании - {profit}")

with open("lesson5_7.json", "w") as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f"Созданный файл с расширением Json имеет следующее содержимое: \n "
          f" {js_str}")
