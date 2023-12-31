"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y
(X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он
называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
задуманные Петей числа.
"""

S = int(input('Введите сумму двух чисел: '))
P = int(input('Введите произведение двух чисел: '))

X = 0
Y = 0
for i in range(1, 1001):
    j = S - i
    if i * j == P:
        X = i
        Y = j
        print(f'Первое число: {X}, второе число: {Y}')
        break
if X == 0 and Y == 0:
    print(f'Числа не найдены')
