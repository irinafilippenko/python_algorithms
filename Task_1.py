# 1. Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа
# должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

profit_list = defaultdict(list)
profit_middle = 0

while True:
    count = int(input('Введите количество предприятий: '))
    if count < 2:
        print('Вы ввели неправильное количество (<2).')
    else:
        break

for index in range(count):
    name = input(f'Введите название предприятия № {index + 1}: ')
    for quarter in range(4):
        profit_list[name].append(int(input(f'Введите значение прибыли предприятия за {quarter + 1} квартал: ')))
        profit_middle += profit_list[name][quarter]
    profit_list[name].append(sum(profit_list[name]))

profit_middle = profit_middle / count

print(f'\nСредняя прибыль предприятий: {profit_middle:.2f}')
print('\nПрибыльные предпиятия: ')

for key in profit_list:
    if profit_list[key][4] >= profit_middle:
        print(f'{key}')
print('-' * 30)

print('Убыточные предпиятия: ')

for key in profit_list:
    if profit_list[key][4] < profit_middle:
        print(f'{key}')
print('-' * 30)
