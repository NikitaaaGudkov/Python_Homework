"""
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет
определенную ценность. В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо
только английские, либо только русские буквы.

*Пример:*
ноутбук
    12
"""

eng_list_1 = ("A", "E", "I", "O", "U", "L", "N", "S", "T", "R")
eng_list_2 = ("D", "G")
eng_list_3 = ("B", "C", "M", "P")
eng_list_4 = ("F", "H", "V", "W", "Y")
eng_list_5 = ("K",)
eng_list_8 = ("J", "X")
eng_list_10 = ("Q", "Z")

eng_dict = {eng_list_1: 1, eng_list_2: 2, eng_list_3: 3, eng_list_4: 4,
            eng_list_5: 5, eng_list_8: 8, eng_list_10: 10}

rus_list_1 = ("А", "В", "Е", "И", "Н", "О", "Р", "С", "Т")
rus_list_2 = ("Д", "К", "Л", "М", "П", "У")
rus_list_3 = ("Б", "Г", "Ё", "Ь", "Я")
rus_list_4 = ("Й", "Ы")
rus_list_5 = ("Ж", "З", "Х", "Ц", "Ч")
rus_list_8 = ("Ш", "Э", "Ю")
rus_list_10 = ("Ф", "Щ", "Ъ")

rus_dict = {rus_list_1: 1, rus_list_2: 2, rus_list_3: 3, rus_list_4: 4,
            rus_list_5: 5, rus_list_8: 8, rus_list_10: 10}

my_str = input('Введите строку на английском или на русском языке: ')
result = 0

if "A" <= my_str[0].upper() <= "Z":
    for symbol in my_str:
        for item in eng_dict.keys():
            if item.__contains__(symbol.upper()):
                result += eng_dict[item]
else:
    for symbol in my_str:
        for item in rus_dict.keys():
            if item.__contains__(symbol.upper()):
                result += rus_dict[item]

print(result)
