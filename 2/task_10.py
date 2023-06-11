"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
некоторые – гербом. Определите минимальное число монеток, которые нужно
перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""
import random

n = int(input("Введите общее число монеток: "))
heads_number = 0
tails_number = 0
result_number = 0
for i in range(0, n):
    tempSide = random.randint(0, 1)
    if tempSide == 0:
        heads_number += 1
    else:
        tails_number += 1
print(f'Число монеток, лежащих вверх орлом: {heads_number}')
print(f'Число монеток, лежащих вверх решкой: {tails_number}')
result_number = heads_number if heads_number < tails_number else tails_number
print(f'Необходимо перевернуть: {result_number}')
