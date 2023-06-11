"""
2. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def division(divisible, divisor):
    return divisible / divisor


while True:
    try:
        first_number = int(input("Введите первое число: "))
        second_number = int(input("Введите второе число: "))
        result = division(first_number, second_number)
    except ZeroDivisionError:
        print("Вы что? Пытаетесь делить на 0!")
    else:
        print(result)
        break
