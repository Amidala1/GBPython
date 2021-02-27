"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""
from functools import reduce
import json
from os import path

current_dir_name = path.dirname(__file__)
file_name = path.join(current_dir_name, r"example_files/Lesson_5_7_1.txt")
new_file_name = path.join(current_dir_name, r"example_files/Lesson_5_7_2.json")

profit_dict = {}
avg_profit = {}
firm_info_list = []

with open(file_name, "r") as f:
    for line in f:
        firm_name, form, gain, exps = line.split()
        profit_dict[firm_name] = int(gain) - int(exps)

# сумма всех прибылей фирм
total_profit = reduce(
    lambda total, amount: total + amount if amount >= 0 else total + 0,
    profit_dict.values()
)
firm_info_list.append(profit_dict)

# кол-во фирм с убытком для вычета их из общего числа
loss_count = len(list(filter(lambda x: x < 0, profit_dict.values())))

avg_profit["average_profit"] = total_profit/(len(profit_dict) - loss_count)
firm_info_list.append(avg_profit)


with open(new_file_name, 'w') as f:
    json.dump(firm_info_list, f)



