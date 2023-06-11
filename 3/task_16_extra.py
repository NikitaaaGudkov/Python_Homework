"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в
массиве A[1..N]. Пользователь в первой строке вводит натуральное число N –
количество элементов в массиве. В последующих строках записаны N целых чисел
Ai. Последняя строка содержит число X

*Пример:*
5
    1 2 3 4 5
    3
    -> 1
"""

N = None
while True:
    try:
        N = int(input("Введите количество элементов в массиве: "))
    except ValueError:
        print("Вы ввели не число!")
    else:
        if N < 1:
            print('Вы ввели не натуральное число!')
            continue
        else:
            break

list_numbers = []
for i in range(1, N + 1):
    list_numbers.append(i)

print(*list_numbers)

X = None
while True:
    try:
        X = int(input("Какое число будем искать в массиве? "))
    except ValueError:
        print("Вы ввели не число!")
    else:
        break

result = 0
for item in list_numbers:
    if item == X:
        result += 1
print(f"-> {result}")
