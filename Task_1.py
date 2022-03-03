number = int(input('Введите трехзначное число: '))

number1 = number // 100
number2 = number % 100 // 10
number3 = number % 10

print(f'Сумма: {number1 + number2 + number3}')
print(f'Произведение: {number1 * number2 * number3}')
