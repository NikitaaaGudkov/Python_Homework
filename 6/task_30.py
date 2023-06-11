"""
Задача 30: Заполните массив элементами арифметической прогрессии. Её первый
элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

first_element = int(input('Введите первый элемент прогрессии: '))
diff = int(input('Введите разность прогрессии: '))
count = int(input('Введите количество элементов прогрессии: '))

result = [first_element + (i - 1) * diff for i in range(1, count + 1)]

print(result)