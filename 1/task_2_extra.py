"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""

number = int(input('Введите трёхзначное число: '))
temp_number = number
result = 0
while temp_number != 0:
    result += temp_number % 10
    temp_number //= 10
print(f"Сумма цифр числа {number} равна {result}")
