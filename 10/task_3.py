"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


my_list = ['attribute', 'класс', 'функция', 'type']
result = list()
for item in my_list:
    byte_word = bytes(item, 'utf-8')
    try:
        if len(item) != len(byte_word):
            raise ValueError
    except ValueError:
        result.append(item)
print('Невозможно записать в байтовом типе с помощью маркировки b'':')
print(result)
