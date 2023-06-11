"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

num = int(input('Введите число n: '))
result = num + (num * 10 + num) + (num * 100 + num * 10 + num)
print(f"n + nn + nnn = {result}")
