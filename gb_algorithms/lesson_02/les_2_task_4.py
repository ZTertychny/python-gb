# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры

number_of_el = int(input('Введите количество элементов: '))
count = 0
res = 0

while count != number_of_el:
    number = float(input('Введите число из ряда: '))
    res += number
    count += 1

print(res)

