# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры

import cProfile
import functools
from sys import setrecursionlimit
setrecursionlimit(10000000)

"""Вариант 1 - цикл """


def find_sum_circle(n):
    res = 0
    number = 1
    for item in range(n):
        res += number
        number /= -2
    return res


print(find_sum_circle(4))
cProfile.run('find_sum_circle(5500)')

"""Вариант 2 - рекурсия"""


def find_summ_of_n(n):
    if n == 1:
        return n
    else:
        return (-1) ** (n - 1) * 1 / (2 ** (n - 1)) + find_summ_of_n(n - 1)


print(find_summ_of_n(4))
cProfile.run('find_summ_of_n(5500)')


"""Вариант 3 - рекурсия + мемоизация из 'коробки' """


@functools.lru_cache()
def find_summ_of_n_with_cache(n):
    if n == 1:
        return n
    else:
        return (-1) ** (n - 1) * 1 / (2 ** (n - 1)) + find_summ_of_n(n - 1)


cProfile.run('find_summ_of_n_with_cache(5500)')



# cProfile.run('find_sum_circle(5500)')                                 ---  Для цикла
# 1    0.001    0.001    0.001    0.001 les_4_task_1.py:11(find_sum_circle)

# "import les_4_task_1" "les_4_task_1.find_sum_circle(500)"
# 1000 loops, best of 5: 49.9 usec per loop



# cProfile.run('find_summ_of_n(5500)')                                  ---  Для рекурсии
# 5500/1    0.069    0.000    0.069    0.069 les_4_task_1.py:26(find_summ_of_n)

# "import les_4_task_1" "les_4_task_1.find_summ_of_n(500)"
# 1000 loops, best of 5: 557 usec per loop




# cProfile.run('find_summ_of_n_with_cache(5500)')                       --- Для рекурсии + мемоизации из "коробки"
# 5499/1    0.068    0.000    0.068    0.068 les_4_task_1.py:26(find_summ_of_n)

# "import les_4_task_1" "les_4_task_1.find_summ_of_n_with_cache(500)"
# 1000 loops, best of 5: 109 nsec per loop



"""Вывод:
Наиболее удобная программа - цикличная, т.к. выполняется быстро и может посчитать значения больше 5500(остальные функции
выкидывают ошибку с переполнением стэка). Затем идет функция с рекурсией и декоратором из functools, timeit показал результат в 109"""


