"""
2) реализовать метакласс. позволяющий создавать всегда один и тот же объект
класса (см. урок)
"""


class TypedMeta(type):
    """Метакласс, создающий список __slots__,
    который будет содержать только аттрибуты типа TypedProperty"""
    a = None

    def __call__(self, *args, **kwargs):
        if self.a == None:
            self.a = super().__call__(*args, **kwargs)
        return self.a


class MyClass(metaclass=TypedMeta):
    """Прикладной пользовательский класс"""

    def method_1(self):
        pass

    def method_2(self):
        print('Небольшая проблема')


obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()
print(obj_1 is obj_3)
