"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
"bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку
str.
str(self) - вызывается функциями str, print и format. Возвращает строковое
представление объекта.
"""


class Worker:
    name = 'name'
    surname = 'surname'
    position = 'position'
    _income = dict()

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = income[0]
        self._income["bonus"] = income[1]

    def __str__(self):
        return f'Полное имя сотрудника: {self.surname} {self.name}'


class Position(Worker):
    def get_full_name(self):
        print(Worker.__str__(self))

    def __str__(self):
        return f'Доход с учетом премии: ' \
               f'{self._income["wage"]} + {self._income["bonus"]} = ' \
               f'{self._income["wage"] + self._income["bonus"]}'

    def get_total_income(self):
        print(self)


user = Position('Никита', 'Гудков', 'Разработчик', (100, 50))
user.get_full_name()
user.get_total_income()
