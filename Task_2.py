# 2. Написать программу сложения и умножения двух положительных целых
# шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
# элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма
# чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
from itertools import zip_longest

hex_numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E',
               '15': 'F', 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
sum_hex = deque()
index_sixteen = 0

number1 = deque(input('Введите первое шестнадцатиричное число: ').upper())
number2 = deque(input('Введите второе шестнадцатиричное число: ').upper())

for numbers in zip_longest(reversed(number1), reversed(number2), fillvalue='0'):
    sum_dec = hex_numbers[numbers[0]] + hex_numbers[numbers[1]]
    sum_hex.appendleft(hex_numbers[str((sum_dec + index_sixteen) % 16)])
    index_sixteen = 1 if sum_dec // 16 else 0

print('\nСумма чисел ', *number1, sep='', end=' ')
print('и ', *number2, sep='', end=' ')
print('равна: ', *sum_hex, sep='')
