year = int(input('Введите год: '))

if (year%400 == 0 or year%4 == 0 and year%100 != 0):
    print('Вы ввели високосный год.')
else:
    print('Вы ввели невисокосный год.')




