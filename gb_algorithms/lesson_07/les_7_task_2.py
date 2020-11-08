# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

array = [random.uniform(0, 50) for _ in range(10)]


def sort_merge(array):
    length = len(array)

    if len(array) == 2 and array[0] > array[1]:
        array[0], array[1] = array[1], array[0]

    elif length > 2:
        left_part = sort_merge(array[:length // 2])
        right_part = sort_merge(array[length // 2:])
        array = left_part + right_part

        for i in range(len(array) - 1):
            min_value = array[i]
            min_index = i

            for j in range(i + 1, len(array)):
                if min_value > array[j]:
                    min_value = array[j]
                    min_index = j

            if min_index != i:
                array[i], array[min_index] = array[min_index], array[i]

    return array


print(sort_merge(array))
