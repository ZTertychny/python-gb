# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

output = ''
el_in_rows = 0

for ind in range(32, 128):
    el_in_rows += 1
    if el_in_rows <= 10:
        output += chr(ind) + ' '
    else:
        output += '\n'
        el_in_rows = 0

print(output)
