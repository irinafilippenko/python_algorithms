# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Введите натуральное число: ')
sum_even = 0
sum_odd = 0

for n in number:
    if int(n) % 2 == 0:
        sum_even += 1
    else:
        sum_odd += 1

print(f'Количество чётных цифр: {sum_even}')
print(f'Количество нечётных цифр: {sum_odd}')
