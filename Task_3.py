# 3. В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

number_array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
min_number = number_array[0]
max_number = number_array[0]
min_index = 0
max_index = 0

print('Исходный массив:\n', *number_array, sep='  ')

for i, number in enumerate(number_array):
    if number < min_number:
        min_number = number
        min_index = i
    if number > max_number:
        max_number = number
        max_index = i
number_array[min_index], number_array[max_index] = number_array[max_index], number_array[min_index]

print('Минимальный и максимальный элементы поменяли местами:\n', *number_array, sep='  ')
