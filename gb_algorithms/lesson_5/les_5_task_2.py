# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque, OrderedDict


class Hexadecimal:

    def __init__(self, one, two):
        self.one = one
        self.two = two
        self.sum = None
        self.mul = None

    def transformer_le_num(self, num):
        hexadecimal = dict(F=15, E=14, D=13, C=12, B=11, A=10)
        hexadecimal = OrderedDict(sorted(hexadecimal.items(), key=lambda x: x[0]))

        num = deque(num)
        for el in range(len(num)):
            for k, v in hexadecimal.items():
                if num[el] == k:
                    num[el] = v

        num.reverse()
        return num

    def retransformer_le_num(self, num):
        hexadecimal = dict(F=15, E=14, D=13, C=12, B=11, A=10)
        hexadecimal = OrderedDict(sorted(hexadecimal.items(), key=lambda x: x[0]))

        for el in range(len(num)):
            for k, v in hexadecimal.items():
                if num[el] == v:
                    num[el] = k

        num = [str(_) for _ in num]
        return ''.join(num)

    def sum_hex(self):
        self.one = self.transformer_le_num(self.one)
        self.two = self.transformer_le_num(self.two)

        self.sum = deque()

        while len(self.one) > len(self.two):
            self.two.append(0)
        while len(self.two) > len(self.one):
            self.one.append(0)
        if len(self.one) == len(self.two):
            self.one.append(0)
            self.two.append(0)

        counter = 0
        while counter != len(self.one):
            temp = int(self.one[counter]) + int(self.two[counter])
            if temp > 15:
                remains = temp - 16
                self.sum.appendleft(remains)
                self.one[counter + 1] = self.one[counter + 1] + 1
            else:
                self.sum.appendleft(temp)
            counter += 1

        if self.sum[0] == 0:
            self.sum.popleft()

        self.sum = self.retransformer_le_num(self.sum)
        return self.sum

    def mul_hex(self, ):
        self.one = self.transformer_le_num(self.one)
        self.two = self.transformer_le_num(self.two)
        self.mul = deque([0] * (len(self.one) + len(self.two)))

        if len(self.two) > len(self.one):
            self.one, self.two = self.two, self.one

        for el_first in range(len(self.two)):
            indx = el_first

            for el_second in self.one:
                temp = int(self.two[el_first]) * int(el_second)
                if temp > 15:
                    remains = temp % 16
                    self.mul[indx] += remains
                    self.mul[indx + 1] += temp // 16
                else:
                    self.mul[indx] += temp
                if self.mul[indx] > 15:
                    rem = self.mul[indx] % 16
                    self.mul[indx + 1] += self.mul[indx] // 16
                    self.mul[indx] = rem

                indx += 1

        self.mul.reverse()
        if self.mul[0] == 0:
            self.mul.popleft()

        self.mul = self.retransformer_le_num(self.mul)
        return self.mul


print('Привет! Введите числа для сложения и умножения в шестнадцетеричной системе')
deq_1 = input('Введите первое число: ').upper()
deq_2 = input('Введите второе число: ').upper()

summ = Hexadecimal(deq_1, deq_2)
print(f'Результат сложения - {summ.sum_hex()}')

multip = Hexadecimal(deq_1, deq_2)
print(f'Результать умножения - {multip.mul_hex()}')
