"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
import random
from timeit import default_timer

from memory_profiler import profile


def deco(func):
    def wrapper(l1, l2):
        start_time = default_timer()
        res = func(l1, l2)
        delta = default_timer() - start_time
        return res, delta

    return wrapper


def fill_list(size):
    result_list = []
    for item in range(size):
        result_list.append(random.randint(1, 10))
    return result_list

@deco
@profile
def get_ordered_unique_elements(l1, l2):
    set1 = set()
    for item in l1:
        set1.add(item)
    set2 = set()
    for item in l2:
        set2.add(item)
    common_set = set1.intersection(set2)
    result_list = list()
    for item in common_set:
        result_list.append(item)
    result_list.sort()
    return result_list


n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))

list1 = fill_list(n)
list2 = fill_list(m)
print(list1)
print(list2)

"""
result = get_ordered_unique_elements(list1, list2)
print(result)
"""
print(get_ordered_unique_elements(list1, list2))
