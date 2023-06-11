"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и
возводит число А в целую степень B с помощью рекурсии.
Пример:
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


def raise_degree(base, power):
    if power == 1:
        return base
    elif power % 2 == 0:
        return raise_degree(base * base, power // 2)
    else:
        return base * raise_degree(base, power - 1)


first_number = int(input('Введите основание степени: '))
second_number = int(input('Введите показатель степени: '))
result = raise_degree(first_number, second_number)
print(result)
