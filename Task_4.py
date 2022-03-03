from random import randint, uniform

print('Введите диапазон для случайного целого числа')
int_number1 = int(input('\tпервое целое число: '))
int_number2 = int(input('\tвторое целое число: '))
print('Введите диапазон для случайного вещественного числа')
float_number1 = float(input('\tпервое вещественное число: '))
float_number2 = float(input('\tвторое вещественное число: '))
print('Введите диапазон для случайного символа')
char1 = input('\tпервый символ: ')
char2 = input('\tвторой символ: ')

int_number = randint(int_number1, int_number2)
float_number = uniform(float_number1, float_number2)
char = chr(randint(ord(char1), ord(char2)))

print(f'Случайное целое число: {int_number}')
print(f'Случайное вещественное число: {float_number}')
print(f'Случайный символ: {char}')