"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый
файл.
"""
from os import path

current_dir_name = path.dirname(__file__)
file_name = path.join(current_dir_name, r"related_files/Lesson_5_4_1.txt")
new_file_name = path.join(current_dir_name, r"related_files/Lesson_5_4_2.txt")

numbers_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", }
processed_list = []

with open(file_name, "r") as f:
    for line in f:
        latin_number, digit_number = line.split(" — ")
        if latin_number in numbers_dict:
            processed_list.append(f"{numbers_dict[latin_number]} — {digit_number}")

with open(new_file_name, "w") as f:
    f.writelines(processed_list)
