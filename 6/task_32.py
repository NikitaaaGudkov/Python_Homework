"""
Задача 32: Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше
заданного максимума)
"""
import random

my_list = [random.randint(1, 10) for i in range(20)]
print(my_list)

min_number = int(input('Введите минимум: '))
max_number = int(input('Введите максимум: '))

index = []
for i in range(len(my_list)):
    if min_number <= my_list[i] <= max_number:
        index.append(i)

print(index)
