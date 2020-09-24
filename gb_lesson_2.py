# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

some_list = ['string', 2, ['another list'], {'type':'dictionary'}]

for _i in some_list:
    print(type(_i))


# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

l_input = input('Fill in list with elements separating them by whitespace: ').split(' ')
l_second = []
l_second.extend(l_input)

for first in range(0, len(l_input) - 1, 2):
    l_input[first + 1] = l_input[first]
    l_input[first] = l_second[first + 1]
print(l_input)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


# Решение с помощью  списка
month = int(input('Write a month: '))
seasons = ['winter', 'spring', 'summer', 'autumn']

if month > 12 or month <= 0:
    print("There isn't such month!")
else:
    if month in range(3, 6):
        print(seasons[1])
    elif month in range(6, 9):
        print(seasons[2])
    elif month in range(9, 12):
        print(seasons[3])
    else:
        print(seasons[0])

# Решение с помощью словаря
month_dict = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}

mont_inp = int(input('Write a month: '))
for k, v in month_dict.items():
    if mont_inp in v:
        print(k)


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.


some_string = input('Write a string separating elements by whitespace: ').split(' ')
i = 0


for element in some_string:
    if len(element) > 10:
        print(f'{i + 1} {element[:10]}')
        i += 1
    else:
        print(f'{i + 1} {element}')
        i += 1

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating = [7, 5, 3, 3, 2]

new_el_rating = int(input('Write new element: '))

for item_rating in rating:
    print(item_rating)
    if new_el_rating > item_rating:
        rating.insert(rating.index(item_rating), new_el_rating)
        break
    elif new_el_rating == item_rating:
        if rating.count(new_el_rating) == 1:
            rating.insert((rating.index(item_rating)) + 1, new_el_rating)
        elif rating.count(new_el_rating) > 1:
            rating.insert((rating.index(item_rating)) + rating.count(new_el_rating), new_el_rating)
        break
    else:
        rating.append(new_el_rating)
        break
print(rating)


# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


dict_product = {}
products_list = []

analytics_dict = {}
analytics_products_list = []
analytics_names_list = []
analytics_prices_list = []
analytics_amounts_list = []
analytics_measures_list = []

number_of_dict = 1

while True:
    act = input('Select your action(fill, exit): ')
    if act == 'fill':
        name = input('Write the name: ')
        dict_product.update({'название': name})
        analytics_products_list.append(name)

        price = input('Write the price: ')
        dict_product.update({'цена': price})
        analytics_prices_list.append(price)

        amount = input('Write amount: ')
        dict_product.update({'количество': amount})
        analytics_amounts_list.append(amount)

        measure = input('Write measure: ')
        dict_product.update({'ед': measure})
        analytics_measures_list.append(measure)

        tuple_product = (number_of_dict, dict_product)
        products_list.append(tuple_product)
        number_of_dict += 1
    else:
        break

analytics_dict = dict([('название', analytics_products_list), ('цена', analytics_prices_list), ('количество', analytics_amounts_list), ('ед', analytics_measures_list)])

print(products_list)

print(analytics_dict)
