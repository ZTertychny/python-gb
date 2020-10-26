# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

l_of_numbers = [random.randint(-100, 100) for _i in range(10)]
print(f'Получившийся массив случайных чисел: {l_of_numbers}')

list_of_negatives = []


for ind_of_el in range(0, len(l_of_numbers)):
    if l_of_numbers[ind_of_el] < 0:
        list_of_negatives.append(ind_of_el)

ind_max_of_neg = list_of_negatives[0]
for el_ind in list_of_negatives:
    if l_of_numbers[el_ind] > l_of_numbers[ind_max_of_neg]:
        ind_max_of_neg = el_ind

print(f'Максимальный отрицательный элемент: {l_of_numbers[ind_max_of_neg]}, имеющий индекс - {ind_max_of_neg} ')

