"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

my_list = ['class', 'function', 'method']
for item in my_list:
    print(f'{item} имеет тип {type(item)} и длину {len(item)}')
    result = bytes(item, 'utf-8')
    print(f'{result} имеет тип {type(result)} и длину {len(result)}')
