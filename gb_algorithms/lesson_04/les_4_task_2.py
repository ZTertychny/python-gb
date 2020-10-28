# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2

import cProfile

""" Первый вариант - решето """


def erot_sieve(number):
    segment = 0
    prime_l = [2]
    sieve = [item for item in range(segment, segment + 200) if item % 2 != 0 and item != 1]

    while number > len(prime_l):

        for indx in range(len(sieve)):
            if sieve[indx] != 0:
                j = indx + sieve[indx]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[indx]
        prime_l.extend([el for el in sieve if el != 0])

        segment += 200
        sieve = [item for item in range(segment, segment + 200) if item % 2 != 0]

        for checker in range(len(sieve)):
            for delimeter in prime_l:
                if sieve[checker] % delimeter == 0:
                    sieve[checker] = 0
                    break
    return prime_l[number - 1]


# print(erot_sieve(1400))

# cProfile.run('erot_sieve(100)')
# 1    0.060    0.060    0.062    0.062 les_4_task_2.py:22(erot_sieve)

# cProfile.run('erot_sieve(1000)')
# 1    0.072    0.072    0.074    0.074 les_4_task_2.py:22(erot_sieve)

# cProfile.run('erot_sieve(10000)')
# 1   10.485   10.485   10.507   10.507 les_4_task_2.py:22(erot_sieve)

# "import les_4_task_2" "les_4_task_2.erot_sieve(100)"
# 100 loops, best of 5: 647 usec per loop

# "import les_4_task_2" "les_4_task_2.erot_sieve(1000)"
# 100 loops, best of 5: 42.1 msec per loop

# "import les_4_task_2" "les_4_task_2.erot_sieve(1500)"
# 100 loops, best of 5: 99 msec per loop




""" Второй вариант решения """


def prime_out(number):
    if number == 1:
        return 2

    prime_list = [3]
    odd = prime_list[-1]
    while len(prime_list) < number:
        check = odd + 2
        odd += 2
        for el in prime_list:
            if check % el == 0:
                break
        else:
            prime_list.append(check)

    return prime_list[number - 2]


# print(prime_out(1400))

# cProfile.run('prime_out(100)')
# 1    0.000    0.000    0.001    0.001 les_4_task_2.py:75(prime_out)

# cProfile.run('prime_out(1000)')
# 1    0.054    0.054    0.055    0.055 les_4_task_2.py:75(prime_out)

# cProfile.run('prime_out(10000)')
# 1    9.178    9.178    9.190    9.190 les_4_task_2.py:75(prime_out)

# "import les_4_task_2" "les_4_task_2.prime_out(100)"
# 100 loops, best of 5: 312 usec per loop

# "import les_4_task_2" "les_4_task_2.prime_out(1000)"
# 100 loops, best of 5: 32.4 msec per loop

# "import les_4_task_2" "les_4_task_2.prime_out(1500)"
# 100 loops, best of 5: 71.8 msec per loop


"""Вывод"""
# Обе функции вызывают себя по разу. Лучшее время показывает второй алгоритм.
