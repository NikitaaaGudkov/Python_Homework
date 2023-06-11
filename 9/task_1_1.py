"""
1) реализовать дескрипторы для любых двух классов
Реализация для первого класса:
"""


class CheckWords:
    def __set__(self, instance, value):
        if isinstance(value, str) and value.isalpha():
            instance.__dict__[self.my_attr] = value
        else:
            raise ValueError('Слово должно содержать только буквы!')

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = CheckWords()
    surname = CheckWords()
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


user = Worker('Никита', 'Гудков', 'Разработчик', (100, 50))
print(user)
