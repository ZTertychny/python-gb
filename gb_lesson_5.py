# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


with open("task_lesson_5.txt", "w") as f_obj:
    while True:
        data_input = input('Write some information: ')
        if data_input:
            f_obj.writelines(data_input + '\n')
        else:
            break


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


with open("task_two_for_lesson_5.txt", "r") as task_file:
    print(f"Количество строк состоавляет: {sum(1 for _i in task_file)}")
    task_file.seek(0)
    n_strin = 1
    for line in task_file:
        print(f"В {n_strin} строке {len(_line.split())} слов")
        n_strin += 1


# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


salary_main = []
number_of_emplyees = 0
average_salary = None

with open("task_three_salary.txt", "r", encoding='utf-8') as third_task_file:
    for line in third_task_file:
        content = line.split('составляет')
        if len(content) > 1:
            salary_main.append(int(content[1]))
            number_of_emplyees += 1
            if int(content[1]) < 20000:
                names = content[0].split()
                print('Фамилия сотрудника чей оклад менее 20 тыс.:', names[1])

average_salary = sum(salary_main) / number_of_emplyees
print(f'Средняя величина дохода сотрудников: {int(average_salary)}')



# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

russian_list = ['Один', 'Два', 'Три', 'Четыре']
ind_ex = 0
new_list = []


with open("task_four_for lesson_5.txt", "r", encoding='utf-8') as f_obj:
    for some_l in f_obj:
        temporary_list = some_l.split()
        temporary_list[0] = russian_list[ind_ex]
        new_list.append(' '.join(temporary_list))
        ind_ex += 1


with open("new_list_four_task.txt", "w", encoding='utf-8') as f_obj_new:
    for new_line in new_list:
        f_obj_new.writelines(new_line + '\n')



# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


import random
n = 0

with open("task_five_for_lesson_5.txt", "w") as task_five:
    while n < 8:
        task_five.write(str(random.randint(1, 20)) + ' ')
        n += 1

with open("task_five_for_lesson_5.txt", "r") as file_five_sum:
    storage = [int(int_num) for int_num in file_five_sum.readline().split()]
    print(f'Сумма чисел равна: {sum(storage)}')



# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

temporary_store = []
keys_list = []
values_list = []
dict_of_subjects = {}
sum_of_hours = 0

with open("task_six_for_leson_5.txt", "r", encoding="utf-8") as task_six_obj:
    for line in task_six_obj:
        temporary_store = line.split()
        values_list = []
        for _v in temporary_store:
            if _v.endswith('(пр)') or _v.endswith('(л)') or _v.endswith('(лаб)'):
                values_list.append(int(_v[:_v.find('(')]))
                sum_of_hours = sum(values_list[:])
        dict_of_subjects.update({temporary_store[0][:-1]: sum_of_hours })
        keys_list.append(temporary_store[0][:-1])

print(dict_of_subjects)

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

res_list = []
dict_firms = {}
dict_average_profit = {}
list_average = []
profit = None

with open("task_seven_for_lesson_5.txt", "r", encoding='utf-8') as task_seven_file:
    for line in task_seven_file:
        temp_storage = line.split()
        profit = int(temp_storage[2]) - int(temp_storage[3])
        dict_firms.update({temp_storage[0]: profit})
        if profit > 0:
            print(f'Прибыль компании {temp_storage[0]} составила {profit} \n')
            list_average.append(profit)
        else:
            print(f'Компания {temp_storage[0]} понесла убытки в размере {abs(profit)} \n')

dict_average_profit.update({'average_profit': int((sum(list_average[:]) / len(list_average)))})

res_list.append(dict_firms)
res_list.append(dict_average_profit)

with open("res_list_task_seven.json", "w") as write_file_json:
    json.dump(res_list, write_file_json)


