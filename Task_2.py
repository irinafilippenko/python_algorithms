# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50). Выведите
# на экран исходный и отсортированный массивы.

from random import random


def create_array(n):
    SIZE = n

    return [round(50 * random(), 2) for _ in range(SIZE)]


def merger_sort_1(array):
    if len(array) > 1:
        middle_index = len(array) // 2
        left_array = array[:middle_index]
        right_array = array[middle_index:]

        merger_sort_1(left_array)
        merger_sort_1(right_array)

        i = j = k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i+=1
            else:
                array[k] = right_array[j]
                j+=1
            k+=1
        while i < len(left_array):
            array[k] = left_array[i]
            i+=1
            k+=1
        while j < len(right_array):
            array[k] = right_array[j]
            j+=1
            k+=1

    return array


def merger_sort_2(array):
        if len(array) > 1:
            result = []
            middle_index = len(array) // 2
            left_array = merger_sort_2(array[:middle_index])
            right_array = merger_sort_2(array[middle_index:])

            i = j = 0

            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    result.append(left_array[i])
                    i += 1
                else:
                    result.append(right_array[j])
                    j += 1
            if i < len(left_array):
                result.extend(left_array[i:])
            if j < len(right_array):
                result.extend(right_array[j:])
            return result
        else:
            return array


array = create_array(10)
print(f'Исходный массив:\n{array}')
print(f'Отсортированный массив по возрастанию:\n{merger_sort_1(array)}')
print(f'Отсортированный массив по возрастанию:\n{merger_sort_2(array)}')