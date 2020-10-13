# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def change_to_int(cls, date):
        cls.date = [int(el) for el in date.split('-')]
        return cls.date

    @staticmethod
    def valid(date):
        date_list = [int(el) for el in date.split('-')]
        if 0 < date_list[0] < 32 and 0 < date_list[1] < 13:
            return date_list
        else:
            return f'Not valid'


print(type(Date.change_to_int('23-03-1997')[0]), '\n')

print(Date.valid('31-03-2019'))

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class Except(Exception):

    def __init__(self, txt):
        self.txt = txt


numerator = int(input('Write numerator: '))
denominator = int(input('Write denominator: '))

try:
    numerator / denominator
except ZeroDivisionError:
    print(Except('Наша остановочка, делишь на ноль'))
else:
    print(f'Ответ: {numerator / denominator}')


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.


class MyError(Exception):

    def __init__(self, msg):
        self.msg = msg


number_list = []
number = None

while True:
    number = input('Write a number: ')
    if number == 'stop':
        break
    else:
        try:
            number_list.append(int(number))
        except ValueError:
            print(MyError("It's not a number"))
print(number_list)


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# +
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# +
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.



class MyExcept(Exception):

    def __init__(self, msg):
        self.msg = msg


class OfficeEquipment:

    def __init__(self, name, directory, information_to_do):
        self.name = name
        self.directory = directory
        self.inf = information_to_do
        self.dict_of_tech = {}

    @classmethod
    def to_storage(cls, printers, scans, xeroxs):
        try:
            int(printers) or int(scans) or int(xeroxs)
        except ValueError:
            return MyExcept('Нельзя вводить строку')
        else:
            cls.dict_of_tech = dict(printers=printers, scans=scans, xeroxs=xeroxs)
            return f'На склад была направлена следующая техника {cls.dict_of_tech}'



class Printer(OfficeEquipment):

    def to_print(self):
        return f'Принтер {self.name}, находящийся в {self.directory}, начал печатать файл {self.inf}\n'


class Scan(OfficeEquipment):

    def __init__(self, name, papers):
        self.name = name
        self.papers = papers
        self.time = int(self.papers) * 15

    def to_scan(self):
        return f'Сканер {self.name} начал свою работу. Приблизительное время сканирования составит {self.time} секунд\n'


class Xerox(OfficeEquipment):

    def to_copy(self):
        return f'Ксерокс {self.name}, расположенный в {self.directory}, начал ксерокопирование. Процесс называется {self.inf}'


# Вывод 4 задания
printer = Printer('R2D2', 'reception', 'review')
print(printer.to_print())

scaner = Scan('S10R301', 5)
print(scaner.to_scan())

xerox = Xerox('POP345', 'first_floor', 'article')
print(xerox.to_copy())

# Вывод 5 задания
to_storage = OfficeEquipment.to_storage('five', 5, 2)
print(to_storage)


# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
# сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''z = a + bi
z = 3 + i
z = 5 - 2i'''

class ComplexNumber:

    def __init__(self, number):
        self.number = number.split()
        self.dict_of_numbers = dict(real_part=int(self.number[0]), imaginary_part=int(self.number[2][:-1]) if len(self.number[2]) > 1 else 1)
        self.imaginary_part = self.number[2][:-1] if len(self.number[2]) > 1 else 1
        self.dict_of_numbers['imaginary_part'] = int(self.dict_of_numbers['imaginary_part'] * 1) if self.number[1] == '+' else int(self.dict_of_numbers['imaginary_part'] * -1)


    def __str__(self):
        if '0i' in self.number:
            return self.number[0]
        elif '1i' in self.number:
            self.number.pop()
            self.number.append('i')
            return ' '.join(self.number)
        else:
            return ' '.join(self.number)

    def __add__(self, other):
        """Сумма комплексных чисел происходит по следующей формуле: (a + bi) + (c + di) = (a + c) + (b + d)i.
        В данном методе вначале складываем вещественные и мнимые части комплексного числа, после чего передаем их классу на вывод"""
        real_part = self.dict_of_numbers['real_part'] + other.dict_of_numbers['real_part']
        imaginary_part = self.dict_of_numbers['imaginary_part'] + other.dict_of_numbers['imaginary_part']
        if imaginary_part >= 0:
            imaginary_part = f'+ {imaginary_part}i'
        else:
            imaginary_part = f'- {str(imaginary_part)[1:]}i'
        return ComplexNumber(f'{real_part} {imaginary_part}')



    def __mul__(self, other):
        """Произведение комлексных чисел происходит по следующей формуле: (a + bi) · (c + di) = ac + bci + adi + bdi2 = (ac - bd) + (bc + ad)i
        В данном методе будем действовать постепенно: получим первую скобку, вторую, передадим классу на вывод"""
        first_parenthesis = (self.dict_of_numbers['real_part'] * other.dict_of_numbers['real_part']) - (self.dict_of_numbers['imaginary_part'] * other.dict_of_numbers['imaginary_part'])
        second_parenthesis = (self.dict_of_numbers['imaginary_part'] * other.dict_of_numbers['real_part']) + (self.dict_of_numbers['real_part'] * other.dict_of_numbers['imaginary_part'])
        if second_parenthesis >= 0:
            second_parenthesis = f'+ {second_parenthesis}i'
        else:
            second_parenthesis = f'- {str(second_parenthesis)[1:]}i'
        return ComplexNumber(f'{first_parenthesis} {second_parenthesis}')






first_number = ComplexNumber('5 - 2i')
print(first_number, '\n')

second_number = ComplexNumber('3 + i')
print(second_number, '\n')

print(first_number + second_number, '\n')
print(first_number * second_number)

