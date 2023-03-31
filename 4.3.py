a=int(input('Введите год рождения'))
b=int(input('Введите месяц рождения'))
c=int(input('Введите день рождения'))
magic=b*c
d=a%100
if d== magic :
    print(magic,'=',d,'Ваша дата магическая')
else:
    print(magic,'=',d,'Ваша дата не магическая')
