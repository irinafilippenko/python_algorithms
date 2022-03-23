# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный»
# и «максимальный отрицательный». Это два абсолютно разных значения.

from random import randint

SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 100

number_array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
max_neg_number = 0
max_neg_index = 0

print('Исходный массив:\n', *number_array, sep='  ')

for i, number in enumerate(number_array):
    if number < 0 and (max_neg_number == 0 or number > max_neg_number):
        max_neg_number = number
        max_neg_index = i

if max_neg_index == 0:
    print('В массиве отсутствуют отрицательные элементы.')
else:
    print(f'Максимальный отрицательный элемент массива {max_neg_number} '
          f'находится на {max_neg_index} позиции.')
