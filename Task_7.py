# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

number_array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Исходный массив:\n', *number_array, sep='  ')

if number_array[0] < number_array[1]:
    min_number_1 = number_array[0]
    min_number_2 = number_array[1]
else:
    min_number_1 = number_array[1]
    min_number_2 = number_array[0]

for number in number_array[2:]:
    if number <= min_number_1:
        min_number_2 = min_number_1
        min_number_1 = number
    elif number <= min_number_2:
        min_number_2 = number

print(f'Минимальные элементы массива {min_number_1} и {min_number_2}.')
