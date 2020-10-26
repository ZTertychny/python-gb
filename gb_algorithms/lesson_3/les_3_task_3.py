# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""Представил два варианта: в первом числа в массиве могут повторяться(максимальные и минимальные), поэтому заменял первый элемент.
   Во втором варианте через множество set избавился от повторений"""

# import random
# min_ind = 0
# max_ind = 0
#
# list_of_int = [random.randint(1, 20) for _i in range(15)]
# print(f'Был сформирован следующий список случайных целых чисел: {list_of_int}\n')
#
# for el in range(0, len(list_of_int)):
#     if list_of_int[el] > list_of_int[max_ind]:
#         max_ind = el
#     if list_of_int[el] < list_of_int[min_ind]:
#         min_ind = el
#
# print(f'Максимальное значение: {list_of_int[max_ind]}, минимальное: {list_of_int[min_ind]}\n')
# max_var = list_of_int[max_ind]
# list_of_int[max_ind] = list_of_int[min_ind]
# list_of_int[min_ind] = max_var
#
#
# print(f'В результате получилось следующее: {list_of_int}')







# ''' Второй вариант'''
#
# min_ind = 0
# max_ind = 0
#
# list_of_int = list(set([random.randint(1, 20) for _i in range(15)]))
# print(f'Был сформирован следующий список случайных целых чисел: {list_of_int}\n')
#
# for el in range(0, len(list_of_int)):
#     if list_of_int[el] > list_of_int[max_ind]:
#         max_ind = el
#     if list_of_int[el] < list_of_int[min_ind]:
#         min_ind = el
#
#
# print(f'Максимальное значение: {list_of_int[max_ind]}, минимальное: {list_of_int[min_ind]}\n')
# max_var = list_of_int[max_ind]
# list_of_int[max_ind] = list_of_int[min_ind]
# list_of_int[min_ind] = max_var
#
# print(f'В результате получилось следующее: {list_of_int}')
