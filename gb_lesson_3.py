# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def some_div(numerator, denominator):
    return numerator / denominator


first_num = int(input('Write numerator: '))
second_num = int(input('Write a denominator: '))

try:
    print(some_div(first_num, second_num))
except ZeroDivisionError:
    print('Деление на ноль')


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def id(name, surname, birth, city, email, phone):
    id_dict = {'name': name, 'surname': surname, 'birth': birth , 'city': city, 'e-mail': email, 'phone': phone}
    print(id_dict)


name_input = input('Write a name: ')
surname_input = input('Write a surname: ')
birth_input = input('Write a date of birth: ')
city_input = input('Write a city: ')
email_input = input('Write an e-mail: ')
phone_input = input('Write a phone: ')

id(name = name_input, surname = surname_input, birth = birth_input, city = city_input, email = email_input, phone = phone_input)



# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(one_arg, two_arg, three_arg):
    numbers_of_lis = [one_arg, two_arg, three_arg]
    numbers_of_lis.remove(min(numbers_of_lis))
    return sum(numbers_of_lis[:])

print(my_func(5,4,3))


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# Первый способ
def my_func_sqrt(x,y):
    return x ** y

print(my_func_sqrt(2,-2))

# Второй способ
def my_func_sqrt(x,y):
    while y != 0:
        res = x
        res = res * x
        if y < 0:
            y += 1
        else:
            y -= 1
    return 1 / res

print(my_func_sqrt(2,-2))

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_of_list(some_list):
    some_list = [int(item) if item != 'stop' else item for item in some_list]
    if 'stop' in some_list:
        return sum(some_list[:some_list.index('stop')])
    else:
        return sum(some_list[:])

res = 0

while True:
    numbers_inp = input().split()
    if 'stop' in numbers_inp:
        break
    else:
        res = res + sum_of_list(numbers_inp)
        print(res)



# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(text):
    return text.title()


print(int_func(input('Write your expressions: ')))

