number1 = float(input('Введите первое число: '))
number2 = float(input('Введите второе число: '))
number3 = float(input('Введите третье число: '))

if number2 < number1 and number1 < number3 or number3 < number1 and number1 < number2:
    print(number1)
elif number1 < number2 and number2 < number3 or number3 < number2 and number2 < number1:
    print(number2)
else:
    print(number3)