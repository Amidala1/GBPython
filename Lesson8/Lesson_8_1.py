"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
import time


class Date:
    user_date: str

    def __init__(self, user_date: str):
        self.user_date = user_date

    @classmethod
    def date_transform(cls, user_date: str):
        validated_date = cls.date_validate(user_date)
        if validated_date:
            return [int(x) for x in user_date.split("-")]
        else:
            return f"Неверный формат входной даты."

    @staticmethod
    def date_validate(user_date: str):
        try:
            return time.strptime(user_date, "%d-%m-%Y")
        except ValueError:
            return None


if __name__ == "__main__":
    try:
        user_date = input("Введите дату в формате «день-месяц-год» для его преобразования: ")
        print(Date.date_transform(user_date))
    except KeyboardInterrupt:
        print("\nРабота программы прекращена")
