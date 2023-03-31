a = input('Введите пароль:')
if len(a) < 5:
    print('Слишком короткий пароль')
elif not ('!'or '@'or '#'or '$'or '%') in a:
    print('Добавьте специальные символы : !@#$ ')
elif a.islower():
    print('Добавьте заглавную букву ')
elif not ('1'or '2'or '3'or '4'or '5'or'6'or '7'or '8'or '9'or '0') in a:
    print('Добавьте цифры в пароль')
else:
    b = input('Введите пароль повторно:')
    if a==b :
        print('Пароль принят')
    else:
        print('Пароли не совпадают')