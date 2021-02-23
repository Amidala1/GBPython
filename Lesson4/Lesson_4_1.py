"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета
для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

name, worked_hours, rate, bonus = argv


def calc_salary(worked_hours: int = 0, rate: int = 0, bonus: int = 0):
    """
    worked_hours: выработка в часах
    rate: ставка в час
    bonus: премия (по умолчанию равно 0)
    """
    return (worked_hours * rate) + bonus


def sanitize_value(value):
    if value.isdigit():
        return int(value)
    else:
        print("Введены некорректные данные")
        exit(1)


print(calc_salary(sanitize_value(worked_hours), sanitize_value(rate), sanitize_value(bonus)))

