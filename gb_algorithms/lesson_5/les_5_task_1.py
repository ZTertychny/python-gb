# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import ChainMap


enter_dict = ChainMap()
number_of_enter = int(input('Введите количество предприятий: '))

average_prof = 0

counter = 0

while counter != number_of_enter:
    name = input('Введите название предприятия: ')
    profit = [int(summ) for summ in input('Введите прибыль за 4 квартала через пробел: ').split()]
    profit = sum(profit)

    dict_of_enter = {name: profit}

    average_prof += profit
    enter_dict = enter_dict.new_child(dict_of_enter)

    counter += 1


average_prof = average_prof / number_of_enter


print(f'Средняя приыбль всех предприятий составила {average_prof}\n')
for dictionary in enter_dict.maps[:-1]:
    for k,v in dictionary.items():
        if v > average_prof:
            print(f'Прибыль {k} выше среднего, составила {v}\n')
        else:
            print(f'Прибыль {k} ниже среднего, составила {v}\n')

