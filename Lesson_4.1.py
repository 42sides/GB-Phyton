import sys
from lesson4 import lesson_4_1_script


try:
    anything, hours, salary, bonus = sys.argv
except ValueError:
    print("Недостаточно значений")
    exit()

lesson_4_1_script.person_salary(int(hours), int(salary), int(bonus))
