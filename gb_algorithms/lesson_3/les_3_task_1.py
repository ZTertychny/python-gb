# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

res = [0] * 8


for num_of_array in range(2, 100):
    for divider in range(2, 10):
        if num_of_array % divider == 0:
            res[divider - 2] += 1

counter = 0
while counter < len(res):
    print(f'Количество чисел, кратных {counter + 2}, - {res[counter]}')
    counter += 1


