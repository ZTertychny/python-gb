# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.


first_var = int(input('Write your number: '))
second_var = input('Write something here: ')

print(first_var)
print(second_var)





# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


seconds_input = int(input('Write the rime in seconds: '))
hours_output = seconds_input // 3600
seconds_input = seconds_input - (3600 * hours_output)
if hours_output < 10:
    hours_output = f'0{hours_output}'
minutes_output = seconds_input // 60
seconds_output = seconds_input - (60 * minutes_output)
if minutes_output < 10:
    minutes_output = f'0{minutes_output}'

print(f'your time is {hours_output}:{minutes_output}:{seconds_output}')





# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

some_number = input('Write your number: ')
print(int(some_number) + int(some_number * 2) + int(some_number * 3))


# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#    Для решения используйте цикл while и арифметические операции.


user_number_input = int(input('Write your number: '))
max_number = 0

while user_number_input > 9:
    remainder = user_number_input % 10
    if max_number < remainder:
        max_number = remainder
    user_number_input = user_number_input // 10
print(max_number)





# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


income_input = int(input('Write income of a company: '))
costs_input = int(input('Write costs of a company: '))

if income_input > costs_input:
    print('Сompany has positive revenue indicators')
    profit = income_input - costs_input
    print(f'Profitability margin of a company is {profit / income_input}\n')
    number_of_employees = int(input('To determine the profit ratio per employee write nubmer of employees: '))
    profit_per_employee = profit / number_of_employees
    print(f'The profit ratio per employee is {profit_per_employee}')
else:
    print('Company has negative revenue indicators')




# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.


distance = int(input('Write the distance: '))
goal_input = int(input('Write the goal: '))
day = 1

while distance < goal_input:
    day += 1
    distance = distance + (distance * 0.1)

print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {goal_input} км')
