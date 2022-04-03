# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Выбрана задача 5 из урока 3.
# первый вариант кода - мой, второй - из урока, третий - с использованием
# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный»
# и «максимальный отрицательный». Это два абсолютно разных значения.

from random import randint
from timeit import timeit
from cProfile import run


def create_array(n):
    SIZE = n
    MIN_ITEM = -100
    MAX_ITEM = 100

    return [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def max_neg_1(n):
    number_array = create_array(n)
    max_neg_number = 0
    max_neg_index = 0

    for i, number in enumerate(number_array):
        if number < 0 and (max_neg_number == 0 or number > max_neg_number):
            max_neg_number = number
            max_neg_index = i

    return max_neg_index, max_neg_number


# print(timeit('max_neg_1(10)', number=100, globals=globals()))         # 0.0007474000000000022
# print(timeit('max_neg_1(100)', number=100, globals=globals()))        # 0.009180300000000002
# print(timeit('max_neg_1(1000)', number=100, globals=globals()))       # 0.0748512
# print(timeit('max_neg_1(10_000)', number=100, globals=globals()))     # 0.6756923
# print(timeit('max_neg_1(100_000)', number=100, globals=globals()))    # 6.7922012
# print(timeit('max_neg_1(1_000_000)', number=100, globals=globals()))  # 72.8020742
# print(timeit('max_neg_1(3_000_000)', number=100, globals=globals()))  # 219.358017
# print(timeit('max_neg_1(20_000_000)', number=100, globals=globals())) # 1413.8099707

# для графика
# print(timeit('max_neg_1(10)', number=100, globals=globals()))      # 0.0007515000000000022
# print(timeit('max_neg_1(25_000)', number=100, globals=globals()))  # 1.8510292000000002
# print(timeit('max_neg_1(50_000)', number=100, globals=globals()))  # 3.4296136000000006
# print(timeit('max_neg_1(75_000)', number=100, globals=globals()))  # 5.4538489
# print(timeit('max_neg_1(100_000)', number=100, globals=globals())) # 6.894041999999999

# run('max_neg_1(1_000_000)')

'''         5272895 function calls in 1.623 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.010    0.010    1.623    1.623 <string>:1(<module>)
        1    0.000    0.000    1.544    1.544 Task_1.py:10(create_array)
        1    0.215    0.215    1.544    1.544 Task_1.py:15(<listcomp>)
        1    0.069    0.069    1.613    1.613 Task_1.py:23(max_neg_1)
  1000000    0.486    0.000    1.059    0.000 random.py:200(randrange)
  1000000    0.270    0.000    1.329    0.000 random.py:244(randint)
  1000000    0.400    0.000    0.573    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    1.623    1.623 {built-in method builtins.exec}
  1000000    0.073    0.000    0.073    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1272889    0.101    0.000    0.101    0.000 {method 'getrandbits' of '_random.Random' objects}'''


def max_neg_2(n):
    number_array = create_array(n)
    i = 0
    max_neg_index = -1

    while i < len(number_array):
        if number_array[i] < 0 and max_neg_index == -1:
            max_neg_index = i
        elif 0 > number_array[i] > number_array[max_neg_index]:
            max_neg_index = i
        i += 1

    return max_neg_index, number_array[max_neg_index]


# print(timeit('max_neg_2(10)', number=100, globals=globals()))         # 0.0008295999999999998
# print(timeit('max_neg_2(100)', number=100, globals=globals()))        # 0.0077074
# print(timeit('max_neg_2(1000)', number=100, globals=globals()))       # 0.10874160000000002
# print(timeit('max_neg_2(10_000)', number=100, globals=globals()))     # 0.7820446999999999
# print(timeit('max_neg_2(100_000)', number=100, globals=globals()))    # 8.3198359
# print(timeit('max_neg_2(1_000_000)', number=100, globals=globals()))  # 85.5386941
# print(timeit('max_neg_2(3_000_000)', number=100, globals=globals()))  # 261.133469
# print(timeit('max_neg_2(20_000_000)', number=100, globals=globals())) # 1634.2873385

# для графика
# print(timeit('max_neg_2(10)', number=100, globals=globals()))      # 0.0008261999999999992
# print(timeit('max_neg_2(25_000)', number=100, globals=globals()))  # 2.1360167
# print(timeit('max_neg_2(50_000)', number=100, globals=globals()))  # 4.1555119000000005
# print(timeit('max_neg_2(75_000)', number=100, globals=globals()))  # 6.260170800000001
# print(timeit('max_neg_2(100_000)', number=100, globals=globals())) # 8.292857300000001

# run('max_neg_2(1_000_000)')

'''         6271928 function calls in 1.847 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.010    0.010    1.847    1.847 <string>:1(<module>)
        1    0.000    0.000    1.544    1.544 Task_1.py:10(create_array)
        1    0.211    0.211    1.544    1.544 Task_1.py:15(<listcomp>)
        1    0.226    0.226    1.837    1.837 Task_1.py:74(max_neg_2)
  1000000    0.490    0.000    1.065    0.000 random.py:200(randrange)
  1000000    0.268    0.000    1.332    0.000 random.py:244(randint)
  1000000    0.401    0.000    0.575    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    1.847    1.847 {built-in method builtins.exec}
  1000001    0.067    0.000    0.067    0.000 {built-in method builtins.len}
  1000000    0.074    0.000    0.074    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1271921    0.101    0.000    0.101    0.000 {method 'getrandbits' of '_random.Random' objects}'''


def max_neg_3(n):
    number_array = create_array(n)
    number_array_neg = [number for number in number_array if number < 0]
    max_neg_number = max(number_array_neg)
    max_neg_index = number_array.index(max_neg_number)
    return max_neg_index, max_neg_number


# print(timeit('max_neg_3(10)', number=100, globals=globals()))         # 0.0025500000000000106
# print(timeit('max_neg_3(100)', number=100, globals=globals()))        # 0.013654700000000006
# print(timeit('max_neg_3(1000)', number=100, globals=globals()))       # 0.0740455
# print(timeit('max_neg_3(10_000)', number=100, globals=globals()))     # 0.739051
# print(timeit('max_neg_3(100_000)', number=100, globals=globals()))    # 6.5004995
# print(timeit('max_neg_3(1_000_000)', number=100, globals=globals()))  # 67.55561499999999
# print(timeit('max_neg_3(3_000_000)', number=100, globals=globals()))  # 200.48748869999997
# print(timeit('max_neg_3(20_000_000)', number=100, globals=globals())) # 1319.9901432000001

# для графика
# print(timeit('max_neg_3(10)', number=100, globals=globals()))      # 0.0010474999999999998
# print(timeit('max_neg_3(25_000)', number=100, globals=globals()))  # 1.6639637999999999
# print(timeit('max_neg_3(50_000)', number=100, globals=globals()))  # 3.2944939
# print(timeit('max_neg_3(75_000)', number=100, globals=globals()))  # 4.8409305
# print(timeit('max_neg_3(100_000)', number=100, globals=globals())) # 6.4351655

# run('max_neg_3(1_000_000)')

'''         5273992 function calls in 1.592 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.008    0.008    1.592    1.592 <string>:1(<module>)
        1    0.000    0.000    1.540    1.540 Task_1.py:10(create_array)
        1    0.000    0.000    1.584    1.584 Task_1.py:129(max_neg_3)
        1    0.038    0.038    0.038    0.038 Task_1.py:132(<listcomp>)
        1    0.212    0.212    1.540    1.540 Task_1.py:15(<listcomp>)
  1000000    0.496    0.000    1.063    0.000 random.py:200(randrange)
  1000000    0.265    0.000    1.328    0.000 random.py:244(randint)
  1000000    0.396    0.000    0.567    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    1.592    1.592 {built-in method builtins.exec}
        1    0.006    0.006    0.006    0.006 {built-in method builtins.max}
  1000000    0.072    0.000    0.072    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1273983    0.099    0.000    0.099    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}'''

'''Все три решения имеют асимптотику O(N).
Все графики - линейные.
«Нехорошие» алгоритмы получились, но мне «засел в голову» пример третьей задачи
с min, max, index.
В третьем решении получается 0(N) * (1 + 0.5 + 0.5), если допустить,
что половина массива - отрицательные числа (создание массива из отрицательных
элементов - 1, нахождение максимального - 0.5, нахождение индекса максимального - 0.5).
Дошла до n = 20 миллионов, но не удалось получить худший результат по времени
у третьего алгоритма.

Второй алгоритм проигрывает по времени. Судя по данным cProfile, в цикле while
постоянно происходит подсчёт длины массива, это добавляет «лишние» операции.
Можно добавить переменную со значением длины массива.
  1000001    0.067    0.000    0.067    0.000 {built-in method builtins.len}

И всё же, смею предположить, что в случае, когда предстоит работа с большим
размером данных, лучше воспользоваться первым вариантом с одним циклом-проходом
по массиву.
Если нет гигантских объемов, то функции python (max, index) отрабатывают быстрее
и есть смысл использовать третий вариант.'''
