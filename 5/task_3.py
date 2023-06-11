"""
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""

from task_2 import data_validation


def reverse_numbers(stringNumber):
    length = len(stringNumber)
    if length <= 1:
        return stringNumber
    number = int(stringNumber)
    right_digit = number % 10
    left_digit = number // (10 ** (length - 1))
    return str(right_digit) + reverse_numbers(stringNumber[1:length - 1]) +\
        str(left_digit)


if __name__ == '__main__':
    user_number = str(data_validation())
    result = reverse_numbers(user_number)
    print(f'Перевернутое число: {result}')
