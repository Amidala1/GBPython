"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

from os import path

current_dir_name = path.dirname(__file__)
file_name = path.join(current_dir_name, r"related_files/Lesson_5_2.txt")

with open(file_name, "r") as f:
    content = f.readlines()

print(f"Количество строк в файле: {len(content)}")
words_count = []
for line in content:
    words_count.append(len(line.split()))

print(f"\nКоличество слов в строках:")
for index, value in enumerate(words_count):
    print(f"{index + 1}-я строка: {value}")
