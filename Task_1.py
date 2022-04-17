# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный
# массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает
# на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна
# остаться сортировка пузырьком. Улучшенные версии сортировки, например,
# расчёской, шейкерная и другие в зачёт не идут.

from random import randint


def create_array(n):
    SIZE = n
    MIN_ITEM = -100
    MAX_ITEM = 100

    return [randint(MIN_ITEM, MAX_ITEM - 1) for _ in range(SIZE)]


def bubble_sort(array):
    n = 1

    while n < len(array):
        is_sorted = True
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        if is_sorted:
            break
        n += 1

    return array


array = create_array(10)

print(f'Исходный массив:\n{array}')
print(f'Отсортированный массив по убыванию:\n{bubble_sort(array)}')
