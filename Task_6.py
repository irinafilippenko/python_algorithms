# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ.

from random import randint


def guess_number(amount):
    number = int(input('Введите число от 0 до 100: '))

    if amount == 1:
        return f'Загаданное число = {rand_number}'

    if number == rand_number:
        return 'Поздравляем, вы отгадали число!'
    elif number > rand_number:
        print(f'Ваше число больше. Осталось попыток: {amount - 1}')
        return guess_number(amount - 1)
    else:
        print(f'Ваше число меньше. Осталось попыток: {amount - 1}')
        return guess_number(amount - 1)


if __name__ == "__main__":
    rand_number = randint(1, 101)
    result = guess_number(10)
    print(result)
