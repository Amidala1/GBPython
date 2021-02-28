"""
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, color: str, name: str, is_police: bool = False):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = 0

    def go(self, speed: int):
        try:
            self.speed = int(speed)
        except ValueError:
            print("Вы ввели некорректное значение для скорости")
        else:
            print(f"Машина поехала. Заданная скорость: {speed} км/ч")

    def stop(self):
        print("Машина остановилась")
        self.speed = 0

    def turn(self, direction):
        print(f"Машина повернула { direction.lower()}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        max_allowed_speed = 60
        if self.speed > max_allowed_speed:
            print("Внимание! Превышена максимальная скорость")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        max_allowed_speed = 40
        if self.speed > max_allowed_speed:
            print("Внимание! Превышена максимальная скорость")


class PoliceCar(Car):
    def __init__(self, color: str, name: str, is_police: bool = True):
        super().__init__(color, name, is_police)


police_car = PoliceCar("White", "Ford Mustang")
police_car.go(60)
police_car.turn("направо")
police_car.show_speed()
police_car.stop()
print(police_car.is_police)

town_car = TownCar("Grey", "Hyundai Getz")
town_car.go(80)
town_car.turn("налево")
town_car.show_speed()
town_car.stop()
print(town_car.is_police)
