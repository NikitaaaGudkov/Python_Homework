"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


def get_ping(query):
    ping = subprocess.Popen(query, stdout=subprocess.PIPE)
    print(ping.stdout)
    for line in ping.stdout:
        res = chardet.detect(line)
        print(line.decode(encoding=res['encoding']))


print('Пинг Яндекса:')
YA_ARGS = ['ping', 'yandex.ru']
get_ping(YA_ARGS)
print('Пинг Ютуба:')
YOU_ARGS = ['ping', 'youtube.com']
get_ping(YOU_ARGS)
