# 6. В одномерном массиве найти сумму элементов, находящихся
# между минимальным и максимальным элементами. Сами минимальный
# и максимальный элементы в сумму не включать.

from random import randint

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100

number_array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
min_number = number_array[0]
max_number = number_array[0]
min_index = 0
max_index = 0
sum_between = 0

print('Исходный массив:\n', *number_array, sep='  ')

for i, number in enumerate(number_array):
    if number < min_number:
        min_number = number
        min_index = i
    if number > max_number:
        max_number = number
        max_index = i

print(f'Минимальный элемент массива {min_number} находится на {min_index} позиции.')
print(f'Максимальный элемент массива {max_number} находится на {max_index} позиции.')

if min_index < max_index:
    number_between = number_array[min_index + 1:max_index]
else:
    number_between = number_array[max_index + 1:min_index]

for number in number_between:
    sum_between += number

print(f'Сумма элементов, находящихся между минимальным и максимальным '
      f'элементами равна {sum_between}.')
