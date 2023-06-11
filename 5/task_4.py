"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтись без создания массива!
"""


def sum_of_series(count, result=0, number=1.0):
    if count == 0:
        return result
    result += number
    number = - number / 2
    return sum_of_series(count - 1, result, number)


def data_validation():
    try:
        number = int(input('Введите количество элементов: '))
    except ValueError:
        print('Вы ввели не натуральное число! Повторите попытку!')
        return data_validation()
    else:
        if number < 1:
            print('Число должно быть натуральным! Повторите попытку!')
            return data_validation()
        return number


if __name__ == '__main__':
    amount = data_validation()
    print(f'Количество элементов - {amount}, '
          f'их сумма - {sum_of_series(amount)}')
