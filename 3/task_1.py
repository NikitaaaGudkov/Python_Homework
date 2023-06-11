"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

list_seasons = ["Зима", "Весна", "Лето", "Осень"]
dict_seasons = {1: "Зима", 2: "Зима", 3: "Зима", 4: "Весна", 5: "Весна",
                6: "Весна", 7: "Лето", 8: "Лето", 9: "Лето", 10: "Осень",
                11: "Осень", 12: "Осень"}


def solve_with_list(number_month, list_of_seasons):
    if 1 <= number_month <= 3:
        return list_of_seasons[0]
    elif 4 <= number_month <= 6:
        return list_of_seasons[1]
    elif 7 <= number_month <= 9:
        return list_of_seasons[2]
    else:
        return list_of_seasons[3]


def solve_with_dict(number_month, dictionary_seasons):
    return dictionary_seasons[number_month]


month = None
while True:
    try:
        month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
    except ValueError:
        print("Вы ввели не целое число!")
    else:
        if month < 1 or month > 12:
            print('Вы ввели целое число, не принадлежащее отрезку от 1 до 12!')
            continue
        else:
            break

print(f'Результат через список: {solve_with_list(month, list_seasons)}')
print(f'Результат через словарь: {solve_with_dict(month, dict_seasons)}')
