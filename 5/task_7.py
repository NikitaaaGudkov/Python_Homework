"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""

from task_4 import data_validation


def sum_of_series(number, result_sum=1):
    if number == 1:
        return result_sum
    return result_sum + sum_of_series(number - 1, result_sum + 1)


user_number = data_validation()
left_number = sum_of_series(user_number)
right_number = int(user_number * (user_number + 1) / 2)
print(f'Левая часть равенства: {left_number}, '
      f'правая часть равенства: {right_number}')
print(left_number == right_number)
