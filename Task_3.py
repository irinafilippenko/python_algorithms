# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

number = int(input('Введите натуральное число: '))
back_number = 0

while number > 0:
    back_number = back_number * 10 + number % 10
    number = number // 10

print(f'Обратное число: {back_number}')
