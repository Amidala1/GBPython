"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
from os import path

current_dir_name = path.dirname(__file__)
file_name = path.join(current_dir_name, r"example_files/Lesson_5_6.txt")

final_dict = {}

with open(file_name, "r") as f:
    for line in f:
        subject_info = line.split()
        subject_name = subject_info[0].replace(":", "")
        lections_hours = subject_info[1].replace("(л)", "").replace("—", "0")
        practice_hours = subject_info[2].replace("(пр)", "").replace("—", "0")
        labs_hours = subject_info[3].replace("(лаб)", "").replace("—", "0")
        final_dict[subject_name] = int(lections_hours) + int(practice_hours) + int(labs_hours)

print(f"Итоговый словарь: {final_dict}")
