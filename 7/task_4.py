"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в
виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая
матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй
матрицы и т.д.
"""


class Matrix:
    list_of_lists = list()

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        temp_string = ''
        for i in range(len(self.list_of_lists)):
            for item in self.list_of_lists[i]:
                temp_string += f'{item}\t\t'
            temp_string += f'\n'
        return temp_string

    def __add__(self, other):
        result_list = list()
        for i in range(len(self.list_of_lists)):
            temp_list = list()
            for j in range(len(self.list_of_lists[i])):
                temp_list.append(
                    self.list_of_lists[i][j] + other.list_of_lists[i][j])
            result_list.append(temp_list)
        return Matrix(result_list)


matrix_1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print('Первая матрица: ')
print(matrix_1)

matrix_2 = Matrix([[-3, -5, -32], [-2, -4, -6], [1, -64, 8]])
print('Вторая матрица: ')
print(matrix_2)

print('Сумма двух матриц: ')
print(matrix_1 + matrix_2)
