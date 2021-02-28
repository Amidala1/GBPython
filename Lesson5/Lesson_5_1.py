"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
from os import path

data = []
current_dir_name = path.dirname(__file__)
file_name = path.join(current_dir_name, r"example_files/Lesson_5_1.txt")

print("Введите построчно данные: ")

while True:
    user_data = input()
    if not user_data:
        break
    else:
        data.append(user_data)

with open(file_name, "w") as f:
    for d in data:
        print(d, file=f)
