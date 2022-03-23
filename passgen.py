import random

lowercase = 'abcdefgihjklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIHJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
special = '!@#$%^&*()-?<>^\'\\/~`'


def passgen(x):

    symbols = lowercase + uppercase + numbers + special
    password = random.choice(lowercase)
    password += random.choice(uppercase)
    password += random.choice(numbers)
    password += random.choice(special)

    for i in range(x-4):
        password += random.choice(symbols)

    password = random.sample(list(password), len(password))

    return password


n = input('Введите кол-во символов пароля: ')

while not n.isdigit() or int(n) < 12:
    n = input('Введите верное значение (число, не менее 12): ')

print('Ваш пароль: ', *passgen(int(n)), sep='')
