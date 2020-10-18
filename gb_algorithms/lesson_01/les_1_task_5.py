# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

place_of_letter = int(input('Введите номер буквы в алфавите: ')) - 1

alphabet = string.ascii_lowercase

letter = alphabet[place_of_letter]

print(f'Ваша буква {letter}')
