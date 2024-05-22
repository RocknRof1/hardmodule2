def password(number):
    list = 'Введите шифр: '
    for i in range(1, number):
        for n in range(i + 1, number):
            if number % (i + n) == 0:
                list += str(i) + str(n)
    return list
print(password(int(input('Введите указанное число: '))))