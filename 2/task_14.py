"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
превосходящие числа N.
"""

N = int(input('Введите верхнюю границу: '))
result = 2
degree = 1
while result < N:
    print(f'2 в степени {degree} равно {result}')
    degree += 1
    result *= 2