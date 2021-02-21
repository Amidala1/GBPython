"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные
аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def user(name, second_name, birth, city, email, tel_number):
    """
    :name name: Имя пользователя
    :second_name second_name: Фамилия
    :birth birth: Год рождения
    :city city: Город проживания
    :email email: Электронный адрес
    :tel_number tel_number: Телефон
    """
    return " ".join([name, second_name, birth, city, email, tel_number])


print(user(name="Luna", second_name="Una", birth="2020", city="Lunberg", email="email@mail.ru", tel_number="666"))
