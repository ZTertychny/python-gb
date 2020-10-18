"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы."""


class Matrix(object):

    def __init__(self, matrix):
        self.matrix = matrix
        self.output = ''
        self.matrix_out = []
        self.temporary = []
        self.lines_storage = []

    def __str__(self):
        for line in self.matrix:
            self.output += str(line) + '\n'
        return self.output + '\n'

    def __add__(self, other):
        for line in range(0, len(self.matrix)):
            self.lines_storage = []
            for el in range(0, len(self.matrix[line])):
                self.temporary = self.matrix[line][el] + other.matrix[line][el]
                self.lines_storage.append(self.temporary)
            self.matrix_out.append(self.lines_storage)
        return Matrix(self.matrix_out)


first_mat = [
    [3, 5, 32],
    [2, 4, 6],
    [-1, 64, 8]
]

second_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9, ]
]

one = Matrix(first_mat)
print(one)

two = Matrix(second_matrix)
print(two)

sum_of_matri = one + two
print(sum_of_matri)

"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, 
которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно. 
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class Vetements(ABC):

    @abstractmethod
    def __init__(self):
        pass


class Clothes():

    def __init__(self, coat_size=None, suit_height=None):
        self.size = coat_size
        self.height = suit_height

    @property
    def consumption_of_coat(self):
        if self.size:
            return f'Количество ткани, затраченной на пошив пальто: {self.size / 6.5 + 0.5:.2f}\n'
        else:
            return f'Данные о пальто отсутствуют'

    @property
    def consumption_of_suit(self):
        if self.height:
            return f'Количество ткани, затраченной на пошив костюма: {self.height * 2 + 0.3:.2f}\n'
        else:
            return f'Данных о костюме отсутствуют'

    def __str__(self):
        if self.size and self.height:
            return f'Общее количество ткани составило: {(self.size / 6.5 + 0.5 + self.height * 2 + 0.3):.2f}\n'
        elif self.size and not self.height:
            return self.consumption_of_coat
        elif self.height and not self.size:
            return self.consumption_of_suit


coat = 15
suit = 190

coat_and_suit = Clothes(coat_size=coat, suit_height=suit)
print(coat_and_suit.consumption_of_coat)
print(coat_and_suit.consumption_of_suit)
print(coat_and_suit)

"""Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: 
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). 
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение 
и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, 
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****."""


class Cell:

    def __init__(self, number_of_cellule):
        self.number_of_cellule = number_of_cellule
        self.rows = None
        self.storage_of_cells = '*' * int(self.number_of_cellule)
        self.counter = 0
        self.graphic_out = ''

    def __add__(self, other):
        return Cell(str(self.number_of_cellule + other.number_of_cellule))

    def __sub__(self, other):
        return Cell(str(self.number_of_cellule - other.number_of_cellule))

    def __mul__(self, other):
        return Cell(str(self.number_of_cellule * other.number_of_cellule))

    def __truediv__(self, other):
        return Cell(str(self.number_of_cellule // other.number_of_cellule))

    def __str__(self):
        if int(self.number_of_cellule) > 0:
            return f'Количество ячеек полученной клетки составляет: {self.number_of_cellule}\n'
        else:
            return f'Количество ячеек двух клеток меньше или равно 0\n'

    def make_order(self, rows):
        self.rows = rows
        if self.storage_of_cells:
            for item in self.storage_of_cells:
                if self.counter < rows:
                    self.counter += 1
                    self.graphic_out += item
                else:
                    self.graphic_out += '\n' + item
                    self.counter = 1
            return f'Структура полученной клетки:\n{self.graphic_out}\n'
        else:
            return f'Отсутствует клетка'


first_cell = Cell(9)
print(first_cell)

second_cell = Cell(10)

division = first_cell / second_cell
print(division)

add = first_cell + second_cell
print(add.make_order(5))

mul = first_cell * second_cell
print(mul, mul.make_order(10))

sub = first_cell - second_cell
print(sub, sub.make_order(4))
