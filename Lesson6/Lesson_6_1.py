"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
from time import sleep


class TrafficLight:
    __color = {"красный": 7, "желтый": 2, "зеленый": 10}

    def running(self):
        count = 0
        while count <= 2:
            for key, value in self.__color.items():
                print(f"Горит {key} свет. Осталось {value} секунд до смены режима")
                sleep(value)
            count += 1


traffic_light = TrafficLight()
print(traffic_light.running())
