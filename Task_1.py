# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM_1 = 2
MAX_ITEM_1 = 99
MIN_ITEM_2 = 2
MAX_ITEM_2 = 9

number_multiples = dict.fromkeys(range(MIN_ITEM_2, MAX_ITEM_2 + 1), 0)
# с помощью dictionary comprehension
# number_multiples = {number: 0 for number in range(MIN_ITEM_2, MAX_ITEM_2 + 1)}
number_array = [number for number in range(MIN_ITEM_1, MAX_ITEM_1 + 1)]

for number in number_array:
    for key in number_multiples:
        if number % key == 0:
            number_multiples[key] += 1

for key, value in number_multiples.items():
    print(f'Число {key} кратно {value} чисел в диапазоне от {MIN_ITEM_1} до {MAX_ITEM_1}')
