"""2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""

count = int(input("Введите количество элементов в массиве: "))
some_list = []
flag = True

while count != 0:
    element = None
    while flag:
        element = input("Введите непустое значение списка: ")
        if element != "":
            flag = False
        else:
            print("Значение не должно быть пустым")

    count -= 1
    some_list.append(element)
    flag = True

if len(some_list) % 2 == 0:
    i = 0
    while i < len(some_list):
        j = some_list[i]
        some_list[i] = some_list[i+1]
        some_list[i+1] = j
        i += 2
else:
    i = 0
    while i < len(some_list) - 1:
        el = some_list[i]
        some_list[i] = some_list[i + 1]
        some_list[i + 1] = el
        i += 2

print(some_list)
