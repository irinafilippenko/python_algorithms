# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 100

number_array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
number_count = dict.fromkeys(set(number_array), 0)

print('Исходный массив:\n', *number_array, sep='  ')

find_count = 0
find_number = 0

for number in number_array:
    number_count[number] += 1
    if number_count[number] > find_count:
        find_count = number_count[number]
        find_number = number

if find_count == 1:
    print('Числа в массиве не повторяются и встречаются по одному разу.')
else:
    print(f'Чаще всего встречается число {find_number} ({find_count} раза).')
