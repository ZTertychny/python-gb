# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры

number_of_el = int(input('Введите количество элементов: '))
res = 0
number = 1

for item in range(number_of_el):
    res += number
    number /= -2

print(res)

