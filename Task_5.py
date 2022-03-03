char1 = input('Введите первую букву: ')
char2 = input('Введите вторую букву: ')

point1 = ord(char1) - 96
point2 = ord(char2) - 96

print(f'Буква «{char1}» занимает {point1} позицию в алфавите')
print(f'Буква «{char2}» занимает {point2} позицию в алфавите')
print(f'Между буквами «{char1}» и «{char2}» {point2 - point1} букв(а)')
