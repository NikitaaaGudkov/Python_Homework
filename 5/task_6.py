"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def get_random_number():
    return random.randint(1, 100)


def data_validation(attempt):
    try:
        user_number = int(
            input(f'Попытка № {attempt}. Введите загаданное число: '))
    except ValueError:
        print('Вы ввели не натуральное число! Повторите попытку!')
        return data_validation(attempt)
    else:
        if user_number < 1 or user_number > 100:
            print('Загаданное число находится в диапазоне от 1 до 100! '
                  'Повторите попытку!')
            return data_validation(attempt)
        return user_number


def guess_number(number, attempt):
    if attempt == 11:
        print(f'Вы не угадали за 10 попыток! Это было число: {number}')
    else:
        user_number = data_validation(attempt)
        if user_number == number:
            print(f'Поздравляю Вы угадали число! Это было число: {number}')
        elif user_number > number:
            print(f'Загаданное число меньше Вашего!')
            guess_number(number, attempt + 1)
        else:
            print(f'Загаданное число больше Вашего!')
            guess_number(number, attempt + 1)


random_number = get_random_number()
guess_number(random_number, 1)
