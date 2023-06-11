"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

my_list = ['разработка', 'администрирование', 'protocol', 'standard']
for item in my_list:
    byte_word = item.encode('utf-8')
    str_word = byte_word.decode('utf-8')
    print(f'{type(item)} {item} -> '
          f'{type(byte_word)} {byte_word} -> '
          f'{type(str_word)} {str_word}')
