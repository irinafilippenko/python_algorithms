# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
# надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100

number_array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Первый массив:\n', *number_array, sep='  ')

number_index = [i for i, number in enumerate(number_array) if number % 2 == 0]
# без list comprehension
# number_index = []
#
# for i, number in enumerate(number_array):
#     if number % 2 == 0:
#         number_index.append(i)
print('Второй массив из индексов чётных элементов первого массива:\n', *number_index, sep='  ')
