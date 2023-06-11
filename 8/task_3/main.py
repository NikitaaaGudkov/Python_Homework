"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

data = {
    "list": [0, 1, 2, 3, 4, 5],
    "integer": 24,
    "dictionary": {
        1: "α",
        2: "β",
        3: "γ"
    }
}

with open('file.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(data, f_n, sort_keys=False, default_flow_style=True,
              allow_unicode=True)

with open('file.yaml', 'r', encoding='utf-8') as f_n:
    yaml_dict = yaml.load(f_n, Loader=yaml.FullLoader)

print(data == yaml_dict)
