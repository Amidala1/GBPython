"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

count_list = []
cycle_list = []
raw_values = [33, 44, 55, 66, 77]


def gen_list_with_count(start_number: int = 1, end_number: int = 10):
    try:
        for value in count(start_number):
            if value >= end_number:
                break
            else:
                count_list.append(value)
        return count_list
    except TypeError:
        print("Введены некорректные данные. Программа завершена")
        exit(1)


def gen_list_with_cycle(count: int = 0, end_number: int = 10):
    try:
        for value in cycle(raw_values):
            if count > end_number:
                break
            cycle_list.append(value)
            count += 1
    except TypeError:
        print("Введены некорректные данные. Программа завершена")
        exit(1)
    else:
        return cycle_list


print(f"Сгенерированный список через count: {gen_list_with_count()}")
print(f"Сгенерированный список через cycle: {gen_list_with_cycle()}")
