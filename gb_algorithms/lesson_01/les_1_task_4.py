# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

import string

first_letter, second_letter = input('Введите две буквы: ')

alphabet = string.ascii_lowercase

index_first = alphabet.find(first_letter)
index_second = alphabet.find(second_letter)

if index_second > index_first:
    letters = index_second - index_first - 1
else:
    letters = index_first - index_second - 1
print(
    f'Первая буква стоит на {index_first + 1} месте в алфавите\nВторая буква стоит на {index_second + 1} месте в алфавите\nМежду буквами расположено {letters} букв')

