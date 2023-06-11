"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
целых неотрицательных чисел. Из всех арифметических операций допускаются только
+1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
    4
"""


def recursive_sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return recursive_sum(a + 1, b - 1)
    else:
        return recursive_sum(a - 1, b + 1)


first_number = int(input('Введите первое целое неотрицательное число: '))
second_number = int(input('Введите второе целое неотрицательное число: '))
result = recursive_sum(first_number, second_number)
print(f'{first_number} + {second_number} = {result}')
