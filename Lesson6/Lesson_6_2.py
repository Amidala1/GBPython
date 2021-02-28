"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:

    def __init__(self, _length: float, _width: float):
        try:
            self._length = float(_length)
            self._width = float(_width)
        except ValueError:
            print("Были введены некорректные значения. Программа завершена")
            exit(0)
        else:
            pass

    def calc_mass(self, mass: float):
        thickness: float = 0.05
        try:
            result = self._length * self._width * float(mass) * thickness
        except TypeError:
            return None
        else:
            return result


road = Road(5000, 20)
print(f"Необходимая масса асфальта в кг: {road.calc_mass(25):.2f}")


