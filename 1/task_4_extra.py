"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали
S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя
и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза
больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10
"""

s = int(input('Введите общее количество журавликов: '))
number_peter = s // 6
number_sergey = number_peter
number_kate = s - (number_peter + number_sergey)
print(f'Петя сделал {number_peter} из них')
print(f'Катя сделала {number_kate} из них')
print(f'Серёжа сделал {number_sergey} из них')
