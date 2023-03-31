try:
    a=int(input('Введите число'))
    b=a%3
except ValueError :
    print('Это не число')
if b==0:
    print('Число кратно 3')
else:
    print('Число не кратно 3')