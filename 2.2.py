a=int(input('Введите номер вашего места:'))
if 0<a<37 :
    if a%2==0:
      print('Ваше место в купе сверху')
    else:
        print('Ваше место в купе снизу')
elif 36<a<55:
    if a%2==0:
        print('Ваше место боковое сверху')
    else:
        print('Ваше место боковое снизу')
else:
    print('Введен неправильный номер места')