"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
"""
import random
from timeit import default_timer
from memory_profiler import profile


def deco(func):
    def wrapper(number):
        start_time = default_timer()
        res = func(number)
        delta = default_timer() - start_time
        return res, delta

    return wrapper


@deco
@profile
def foo(N):
    berries = list()
    for item in range(N):
        berries.append(random.randint(1, 10))
    berries = tuple(berries)
    print(f'Количество ягод на каждом кусте: {berries}')
    result = 0
    for index in range(-1, len(berries) - 1):
        temp_sum = berries[index - 1] + berries[index] + berries[index + 1]
        if result < temp_sum:
            result = temp_sum
    return result


N_ = int(input('Введите количество кустов: '))
print(foo(N_))
