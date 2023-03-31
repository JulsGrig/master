try:
    a=int(input('Введите число'))
    b=100/a
except ValueError :
    print('Это не число')
except ZeroDivisionError:
    print('Это число - 0')

print(b)
