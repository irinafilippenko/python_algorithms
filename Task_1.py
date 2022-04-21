# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество
# различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# >>> func("papa")
# 6
# >>> func("sova")
# 9

from hashlib import sha1
from collections import defaultdict


def find_substring(input_string):
    # array_hex_substring = []
    # dict_hex_substring = defaultdict(int)
    set_hex_substring = set()

    for i in range(1, len(input_string)):
        for j in range(len(input_string) - i + 1):
            hex_substring = sha1(input_string[j:j + i].encode('utf-8')).hexdigest()
            # if hex_substring not in array_hex_substring:
            #     array_hex_substring.append(hex_substring)
            # dict_hex_substring[hex_substring] += 1
            set_hex_substring.add(hex_substring)

    # return len(array_hex_substring)
    # return len(dict_hex_substring)
    return len(set_hex_substring)


input_string = input('Введите строку: ')
print(f'Количество различных подстрок в этой строке: {find_substring(input_string)}')
