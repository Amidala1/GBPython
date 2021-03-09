"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""
from sys import exit


class MyZeroDivException(Exception):
    def __str__(self):
        return "Деление на нуль!"


class Operations:
    @staticmethod
    def division(number1: int, number2: int):
        if number2 == 0:
            raise MyZeroDivException
        else:
            return f"{number1} / {number2} = {number1 / number2}"


try:
    number_1, number_2 = int(input("Введите делимое: ")), int(input("Введите делитель: "))
except ValueError:
    print("Вы ввели некорректные данные")
except KeyboardInterrupt:
    print("\nРабота программы прекращена")
else:
    try:
        print(Operations.division(number_1, number_2))
    except MyZeroDivException as e:
        print(e)
        exit(1)
