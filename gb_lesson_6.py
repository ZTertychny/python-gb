# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.
import time


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        self.color = input()
        if self.color == 'красный':
            print(f'{self.color} \nЖдите 7 секунд')
            time.sleep(7)
            print('желтый \nЖдите 2 секунд')
            time.sleep(2)
            print('зеленый \nЖдите 5 секунд')
            time.sleep(5)
        elif self.color == 'желтый':
            print('желтый \nЖдите 2 секунд')
            time.sleep(2)
            print('зеленый \nЖдите 5 секунд')
            time.sleep(5)
        elif self.color == 'зеленый':
            print('зеленый \nЖдите 5 секунд')
            time.sleep(5)
        else:
            print('Сбой режима светофора')


some_color = TrafficLight()
some_color.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см *
# число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_of_asphalt(self):
        return f'{self.__length}м * {self.__width}м * 25кг * 5см = {int(self.__length * self.__width * 25 * 5 / 1000)} т'

asphault = Road(20, 5000)
print(asphault.mass_of_asphalt())


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self):
        self.name = 'Felix'
        self.surname = 'Dzershinskiy'
        self.position = 'Head of Cheka'
        self.dict_income = {'wage': 1000 , 'bonus': 500}
        self._income = sum(self.dict_income.values())

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income

human = Position()
print(f'Доход составляет: {human.get_total_income()}')
human = Position()
print(f'Имя Фамилия сотрудника: {human.get_full_name()}')


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True if is_police else False
        self.direction = None

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула {self.direction}')

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы двигаетесь со скоростью {self.speed}\nСбавьте скорость! Вам разрешено передвигаться со скорость 60 км/ч')
        else:
            print(f'Вы двигаетесь со скоростью {self.speed}')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы двигаетесь со скоростью {self.speed}\nСбавьте скорость! Вам разрешено передвигаться со скоротсью 40 км/ч')
        else:
            print(f'Вы двигаетесь со скоростью {self.speed}')

class PoliceCar(Car):
    pass

class SportCar(Car):
    pass



work_car = WorkCar(50,'green', 'milk')
work_car.show_speed()

police_car = PoliceCar(70, 'black', 'thunder', is_police=True)
police_car.go()

sport_cat = SportCar(100, 'red', 'MqQuin')
sport_cat.stop()

town_car = TownCar(65, 'white', 'Jack')
town_car.show_speed()


# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Мы рисуем с помощью {self.title}')

class Handler(Stationery):
    def draw(self):
        print(f'Как насчет порисовать {self.title}')


pen = Pen('ручкой')
pen.draw()
pencil = Pencil('карандаша')
pencil.draw()
handler = Handler('маркером')
handler.draw()
