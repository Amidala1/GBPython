"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
"""

numbers_sum = 0


def calc_sum(inp_list):
    numb_sum = 0
    for value in inp_list:
        try:
            numb_sum += int(value)
        except ValueError:
            pass

    return numb_sum


while True:
    input_list = (input("Введите числа, разделяя их пробелами: ").lower()).split(" ")
    if "q" in input_list:
        q_index = input_list.index("q")
        numbers_sum += calc_sum(input_list[:q_index])
        print(f"Сумма введеных Вами чисел: {numbers_sum}. Программа завершена")
        exit(0)
    else:
        numbers_sum += calc_sum(input_list)
        print(f"Сумма введеных Вами чисел: {numbers_sum}")
