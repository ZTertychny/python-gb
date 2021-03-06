# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
print('Вводим координаты точки А(x1;y1)')
x1 = float(input('Введите координаты по оси Х первой точки: '))
y1 = float(input('Введите координаты по оси У первой точки: '))

print('\nВводим координаты точки B(x2;y2)')
x2 = float(input('Введите координаты по оси Х второй точки: '))
y2 = float(input('Введите координаты по оси У второй точки: '))

k = (y1 - y2) / (x1 - x2)

b = y2 - k * x2

if b > 0:
    print(f'Уравнение прямой, проходящей через точки A({x1};{y1}) и B({x2};{y2}): y = {k:.2f}x + {b:.2f}')
elif b < 0:
    print(f'Уравнение прямой, проходящей через точки A({x1};{y1}) и B({x2};{y2}): y = {k:.2f}x {b:.2f}')
else:
    print(f'Уравнение прямой, проходящей через точки A({x1};{y1}) и B({x2};{y2}): y = {k:.2f}x')
