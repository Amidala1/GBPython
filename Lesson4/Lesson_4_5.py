"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce


numbers_list = [x for x in range(100, 1001) if (x % 2 == 0)]

numbers_multi_total = reduce(
    lambda total, value: total * value,
    numbers_list
)

print(f"Исходный список: {numbers_list}\nРезультат произведения всех элементов списка: {numbers_multi_total}")
