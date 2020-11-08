# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

array = [random.randint(-100, 100) for i in range(10)]
random.shuffle(array)
print(f'Исходный массив: {array}')


# Изначальный код сортировки пузырьком
# def sort_buble(array):
#     counter = 1
#     while counter < len(array):
#         for i in range(len(array) - counter):
#             if array[i] > array[i + 1]:
#                 array[i], array[i + 1] = array[i + 1], array[i]
#         counter += 1
#         print(array)
#     return array

# Новая версия
def sort_buble_new(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    return array


print(f'Получившийся: {sort_buble_new(array)}')
