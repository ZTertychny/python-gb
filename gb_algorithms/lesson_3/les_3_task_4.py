# Определить, какое число в массиве встречается чаще всего.
"""Сделал вариант, в котором, если несколько чисел встречаются большего всего, то выводит их все"""
import random


list_of_num = [random.randint(1, 10) for _i in range(15)]
print(f'Получившийся массив случайных чисел: {list_of_num}')

res_l = [0] * len(list_of_num)
max_ind = 0
indices_of_max_num = []

for ind_el in range(0, len(list_of_num) - 2):
    frequency = 1
    for ind in range(ind_el + 1, len(list_of_num)):
        if list_of_num[ind_el] == list_of_num[ind]:
            frequency += 1
    res_l[ind_el] = frequency

for max_el in range(0, len(res_l)):
    if res_l[max_el] > res_l[max_ind]:
        max_ind = max_el

for el in range(0, len(res_l)):
    if res_l[max_ind] == res_l[el]:
        indices_of_max_num.append(el)

# print(f'{res_l} \n') --- Выводит массив с указанием, сколько раз повторяется число. Индексы данного массива совпадают с индексами
# массива исходного


if len(indices_of_max_num) > 1:
    print('Наибольшее количество раз встречаются следующие числа:')
    for out in indices_of_max_num:
        print(f'{list_of_num[out]} повторяется {res_l[max_ind]} раз(-а)')
else:
    print(f'Число {list_of_num[max_ind]} встречается чаще всего - {res_l[max_ind]} раз(-a)')
