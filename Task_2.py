# 2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
#
# sieve(2)
# 3
# prime(4)
# 7
# sieve(5)
# 11
# prime(1)
# 2

from math import log
from timeit import timeit
from cProfile import run


def end_sieve(k):
    return int(1.25506 * k * log(k)) + 3


def sieve(k):
    n = end_sieve(k)
    sieve_array = [i for i in range(n)]
    HOLE = 0
    sieve_array[1] = HOLE

    for i in range(2, n):
        if sieve_array[i] != HOLE:
            j = i + i
            while j < n:
                sieve_array[j] = HOLE
                j += i

    index = 0
    for item in sieve_array:
        if item != HOLE:
            index += 1
            if index == k:
                return item


def prime(k):
    find_number = 2
    index = 1

    while (index < k):
        find_number += 1
        j = 0
        for i in range(2, find_number // 2 + 1):
            if (find_number % i == 0):
                j = j + 1
        if (j <= 0):
            index += 1

    return find_number


# print(sieve(2))
# print(prime(4))
# print(sieve(5))
# print(prime(1))

# для графика
# print(timeit('sieve(1)', number=100, globals=globals()))        # 0.0001131000000000014
# print(timeit('sieve(1_000)', number=100, globals=globals()))    # 0.23624429999999996
# print(timeit('sieve(2_000)', number=100, globals=globals()))    # 0.5796779
# print(timeit('sieve(3_000)', number=100, globals=globals()))    # 0.9520089999999999
# print(timeit('sieve(4_000)', number=100, globals=globals()))    # 1.2900991000000002
# print(timeit('sieve(5_000)', number=100, globals=globals()))    # 1.7764839999999995
# print(timeit('sieve(6_000)', number=100, globals=globals()))    # 2.0174514000000006
# print(timeit('sieve(7_000)', number=100, globals=globals()))    # 2.5433459999999997
# print(timeit('sieve(8_000)', number=100, globals=globals()))    # 2.9878894000000003
# print(timeit('sieve(9_000)', number=100, globals=globals()))    # 3.284862499999999
# print(timeit('sieve(10_000)', number=100, globals=globals()))   # 3.667104499999999
# print(timeit('sieve(11_000)', number=100, globals=globals()))   # 4.219265799999999
# print(timeit('sieve(12_000)', number=100, globals=globals()))   # 4.946746300000001
# print(timeit('sieve(13_000)', number=100, globals=globals()))   # 5.161461900000003
# print(timeit('sieve(14_000)', number=100, globals=globals()))   # 5.8628979
# print(timeit('sieve(15_000)', number=100, globals=globals()))   # 6.351285599999997
# print(timeit('sieve(16_000)', number=100, globals=globals()))   # 6.5997883
# print(timeit('sieve(17_000)', number=100, globals=globals()))   # 7.4210104
# print(timeit('sieve(18_000)', number=100, globals=globals()))   # 7.663918600000002
# print(timeit('sieve(19_000)', number=100, globals=globals()))   # 8.502240999999998
# print(timeit('sieve(20_000)', number=100, globals=globals()))   # 9.117587

# run('sieve(20_000)')

'''7 function calls in 0.103 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.103    0.103 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Task_2.py:23(end_sieve)
        1    0.090    0.090    0.101    0.101 Task_2.py:26(sieve)
        1    0.011    0.011    0.011    0.011 Task_2.py:28(<listcomp>)
        1    0.000    0.000    0.103    0.103 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''

# print(timeit('prime(1)', number=100, globals=globals()))      # 0.000027100000000002122
# print(timeit('prime(100)', number=100, globals=globals()))    # 0.32750680000000004
# print(timeit('prime(200)', number=100, globals=globals()))    # 1.6863086999999999
# print(timeit('prime(300)', number=100, globals=globals()))    # 5.3333905999999995
# print(timeit('prime(400)', number=100, globals=globals()))    # 10.0524771
# print(timeit('prime(500)', number=100, globals=globals()))    # 17.148769499999997
# print(timeit('prime(600)', number=100, globals=globals()))    # 28.252281599999996
# print(timeit('prime(700)', number=100, globals=globals()))    # 42.124658
# print(timeit('prime(800)', number=100, globals=globals()))    # 55.646403099999986
# print(timeit('prime(900)', number=100, globals=globals()))    # 73.2839066
# print(timeit('prime(1000)', number=100, globals=globals()))   # 91.4892327
# print(timeit('prime(1100)', number=100, globals=globals()))   # 112.83768690000005
# print(timeit('prime(1200)', number=100, globals=globals()))   # 136.65541580000001
# print(timeit('prime(1300)', number=100, globals=globals()))   # 171.0636743
# print(timeit('prime(1400)', number=100, globals=globals()))   # 203.61004149999997
# print(timeit('prime(1500)', number=100, globals=globals()))   # 228.62029719999998
# print(timeit('prime(1600)', number=100, globals=globals()))   # 264.16129909999995
# print(timeit('prime(1700)', number=100, globals=globals()))   # 313.29739400000017
# print(timeit('prime(1800)', number=100, globals=globals()))   # 343.3964417000002
# print(timeit('prime(1900)', number=100, globals=globals()))   # 386.6462044
# print(timeit('prime(2000)', number=100, globals=globals()))   # 436.5738394
# print(timeit('prime(2100)', number=100, globals=globals()))   # 498.66275429999996
# print(timeit('prime(2200)', number=100, globals=globals()))   # 576.8866772000001
# print(timeit('prime(2300)', number=100, globals=globals()))   # 637.7214783
# print(timeit('prime(2400)', number=100, globals=globals()))   # 703.2554907999997
# print(timeit('prime(2500)', number=100, globals=globals()))   # 767.0217105000002

# run('prime(2500)')

'''4 function calls in 7.696 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    7.696    7.696 <string>:1(<module>)
        1    7.696    7.696    7.696    7.696 Task_2.py:46(prime)
        1    0.000    0.000    7.696    7.696 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''

'''Первое решение (sieve) с помощью алгоритма «Решето Эратосфена» имеет асимптотику O(n).
График - линейный.
Второе решение с нахождением простого числа (prime) имеет асимптотику 0(n**2):
поскольку используется цикл в цикле
while (index < k):
    ...
    for i in range(2, find_number // 2 + 1):

Второй алгоритм заметно проигрывает по времени уже на небольших объемах данных.
Эффективность решения с помощью алгоритма «Решето Эратосфена» очевидна.

print(timeit('sieve(1)', number=100, globals=globals()))        # 0.0001131000000000014
print(timeit('sieve(2_000)', number=100, globals=globals()))    # 0.5796779

print(timeit('prime(1)', number=100, globals=globals()))      # 0.000027100000000002122
print(timeit('prime(2000)', number=100, globals=globals()))   # 436.5738394'''
