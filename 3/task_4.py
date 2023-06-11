"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_1(number_1, number_2, number_3):
    my_list = [number_1, number_2, number_3]
    my_list.sort()
    return my_list[1] + my_list[2]


def my_func_2(number_1, number_2, number_3):
    if number_1 > number_2:
        first_addend = number_1
        second_addend = number_2
    else:
        first_addend = number_2
        second_addend = number_1

    if number_3 > second_addend:
        second_addend = number_3

    return first_addend + second_addend


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))

print(my_func_1(first_number, second_number, third_number))
print(my_func_2(first_number, second_number, third_number))
