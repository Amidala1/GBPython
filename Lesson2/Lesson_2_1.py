"""1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе."""

some_string = "Some String"
number = 1
some_tuple = (2, 4)
some_set = {2, 4}
boolean = True

some_list = [some_string, number, some_tuple, some_set, boolean]

for i in some_list:
    print(type(i))
