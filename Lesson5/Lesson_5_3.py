"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее
10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

from os import path

current_dir_name = path.dirname(__file__)
file_name = path.join(current_dir_name, r"example_files/Lesson_5_3.txt")

threshold = 20000
lower_list = []
higher_list = []
total_salary = 0

with open(file_name, "r") as f:
    content = f.readlines()

for line in content:
    employee_data = line.split()
    surname = employee_data[0]
    salary = employee_data[1]
    if float(salary) < threshold:
        lower_list.append(surname)
    total_salary += float(salary)

print("Сотрудники с окладом ниже 20 тысяч:\n{}\n\nСредний доход сотрудников: {}".format('\n'.join(lower_list),
                                                                                        total_salary / len(content)))
