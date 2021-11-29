def person_salary(work_hours, hour_salary, f_bonus):
    try:
        print(work_hours * hour_salary + f_bonus)
    except TypeError:
        return
