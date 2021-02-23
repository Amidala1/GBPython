"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from random import randint

start_number = 1
end_number = 1000
el_count = 9

numbers_list = [randint(start_number, end_number) for x in range(el_count)]
new_numbers_list = [value for index, value in enumerate(numbers_list) if (index > 0) and
                    (numbers_list[index] > numbers_list[index - 1])]

print(f"Исходный список: {numbers_list}\nОбработанный список: {new_numbers_list}")

