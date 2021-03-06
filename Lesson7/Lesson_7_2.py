"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod
from sys import exit


class AbstractClothes(ABC):
    clothing_param: float
    consumption: float

    def __init__(self, clothing_param):
        self.clothing_param = clothing_param
        self.consumption = 0

    # метод для определения расхода ткани
    @abstractmethod
    def calc_material(self):
        pass


class Suit(AbstractClothes):
    """Костюм"""

    @property
    def calc_material(self):
        return 2 * self.clothing_param + 0.3

    def __str__(self):
        return f"Суммарный расход ткани на производство костюма на рост {self.clothing_param} см.: " \
               f" {self.calc_material} кв.см."


class Coat(AbstractClothes):
    """Пальто"""

    @property
    def calc_material(self):
        return round(self.clothing_param / 6.5 + 0.5, 2)

    def __str__(self):
        return f"Суммарный расход ткани на производство пальто размером {self.clothing_param}: " \
               f" {self.calc_material} кв.м."


# функция для валидации введенного пользователем значения
def validate_user_input(hello_text):
    while True:
        try:
            value = float(input(hello_text))
        except ValueError:
            print("Пожалуйста, введите корректное значение")
        else:
            return value


if __name__ == "__main__":
    exit_flag = False
    while not exit_flag:
        try:
            user_choice = input("Введите 1 - для расчета ткани на производство костюма, 2 - на производство пальто, "
                                "q - для выхода из программы: ")
            if user_choice == "1":
                height = validate_user_input("Введите рост в см.: ")
                suit = Suit(height)
                print(suit)  # Суммарный расход ткани на производство костюма на рост ...:  ... кв.см.
            elif user_choice == "2":
                size = validate_user_input("Введите размер в м.: ")
                coat = Coat(size)
                print(coat)  # Суммарный расход ткани на производство пальто размером ...:  ... кв.м.
            elif user_choice.lower() == "q":
                print("\nВы вышли из программы")
                exit(0)
            else:
                print("Введите одно из предложенных значений: 1, 2 или q")
        except KeyboardInterrupt:
            print("\nВы вышли из программы")
            exit(0)
