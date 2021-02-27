"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from os import path

current_dir_name = path.dirname(__file__)
file_name = path.join(current_dir_name, r"related_files/Lesson_5_5.txt")

user_input = input("Введите числа, разделяя их пробелами: ")
numbers_sum = 0

with open(file_name, "w") as f:
    f.write(user_input)

with open(file_name, "r") as f:
    content = f.read().split()
    for value in content:
        if value.isdigit():
            numbers_sum += int(value)

print(f"Сумма чисел в файле: {numbers_sum}")
