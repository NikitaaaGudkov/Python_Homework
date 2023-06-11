"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
к заданному числу X. Пользователь в первой строке вводит натуральное число N –
количество элементов в массиве. В последующих строках записаны N целых чисел
Ai. Последняя строка содержит число X

*Пример:*
5
    1 2 3 4 5
    6
    -> 5
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
        X = int(input("К какому числу в массиве будем искать ближайшее? "))
    except ValueError:
        print("Вы ввели не число!")
    else:
        break

result = None
if X < 1:
    result = list_numbers[0]
elif X > N:
    result = list_numbers[len(list_numbers) - 1]
else:
    result = X

print(f"-> {result}")
