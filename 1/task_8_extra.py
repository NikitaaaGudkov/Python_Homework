"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
отломить k долек, если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""

first_size = int(input('Введите количество долек первой стороны шоколадки: '))
second_size = int(input('Введите количество долек второй стороны шоколадки: '))
remains = int(input('Введите количество долек, которые нужно отломить: '))
result = False
first_part = 0
second_part = 0
for i in range(first_size // 2):
    first_part = (i + 1) * second_size
    second_part = (first_size - i - 1) * second_size
    if (remains < first_part) and (remains < second_part):
        break
    elif (remains == first_part) or (remains == second_part):
        result = True
        break
if not result:
    for i in range(second_size // 2):
        first_part = (i + 1) * first_size
        second_part = (second_size - i - 1) * first_size
        if (remains < first_part) and (remains < second_part):
            break
        elif (remains == first_part) or (remains == second_part):
            result = True
            break
print(result)
