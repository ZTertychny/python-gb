# Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random
import string

req = input('1 - случайное целое число\n2 - случайное вещественное число\n3 - случайный символ\nВыберите действие: ')

if req == '1':
    start = int(input('Введите нижний предел диапазона: '))
    stop = int(input('Введите верхний предел диапазона: '))
    print(f'Результат - {random.randint(start, stop)}')
elif req == '2':
    start = float(input('Введите нижний предел диапазона: '))
    stop = float(input('Введите верхний предел диапазона: '))
    print(f'Результат - {random.uniform(start, stop):.2f}')
else:
    alphabet = string.ascii_lowercase
    start = input('Введите нижний предел диапазона: ')
    start = start.lower()
    stop = input('Введите верхний предел диапазона: ')
    stop = stop.lower()
    index_start = alphabet.find(start)
    index_stop = alphabet.find(stop)
    rand_index = random.randint(index_start, index_stop)
    print(f'Результат - {alphabet[rand_index]}')
