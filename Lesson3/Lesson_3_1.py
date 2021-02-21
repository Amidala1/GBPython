"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(num1, num2):
    """
    Функция для расчета деления двух чисел
    """
    try:
        return round(num1/num2, 2)
    except ZeroDivisionError:
        return "Деление на ноль!"


print("*** Программа деления двух чисел ***")
while True:
    try:
        number1 = int(input("Введите первое число: "))
        number2 = int(input("Введите второе число: "))
    except ValueError:
        print("Введите числовое значение")
    else:
        print(division(number1, number2))
        break
