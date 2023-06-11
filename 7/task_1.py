"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод
running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета используйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
    __color = "красный"

    def running(self):
        print(TrafficLight.__color)
        sleep(7)
        TrafficLight.__color = 'желтый'
        print(TrafficLight.__color)
        sleep(2)
        TrafficLight.__color = 'зеленый'
        print(TrafficLight.__color)
        sleep(5)
        TrafficLight.__color = 'красный'


traffic_light = TrafficLight()
traffic_light.running()
