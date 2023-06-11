"""
1) реализовать дескрипторы для любых двух классов
Реализация для второго класса:
"""


class CheckNumbers:
    def __set__(self, instance, value):
        if (isinstance(value, float) or isinstance(value, int)) and value > 0:
            instance.__dict__[self.my_attr] = value
        else:
            raise ValueError(
                'Значение должно содержать только положительное число!')

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    unit_mass = 25
    thickness = 0.05
    _length = CheckNumbers()
    _width = CheckNumbers()

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        return self._length * self._width * self.unit_mass * self.thickness


road = Road(-5000, 20.0)
print(road.calc_mass())
