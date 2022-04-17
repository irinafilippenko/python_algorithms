# 3). Массив размером 2m + 1, где m — натуральное число, заполнен
# случайным образом. Найдите в массиве медиану. Медианой называется
# элемент ряда, делящий его на две равные части: в одной находятся
# элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который
# не рассматривался на уроках (сортировка слиянием также недопустима).

from random import randint


def create_array(n):
    M = n
    MIN_ITEM = 0
    MAX_ITEM = 100

    return [randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * M + 1)]


def median(array, index=0):
    if len(array) < 3:
        return array[0]

    left_len = 0
    right_len = 0
    for number in array:
        if number < array[index]:
            left_len += 1
        if number > array[index]:
            right_len += 1

    middle_index = len(array) // 2

    if left_len == middle_index or right_len == middle_index or left_len == right_len:
        return array[index]
    elif left_len < middle_index:
        index += 1
        while array[index - 1] > array[index]:
            index += 1
        return median(array, index)
    else:
        index += 1
        while array[index - 1] < array[index]:
            index += 1
        return median(array, index)


array = create_array(5)

print(f'Исходный массив:\n{array}')
print(f'Медиана списка: {median(array)}')

array.sort()

print(f'\nОтсортированный массив (для наглядности):\n{array}')
