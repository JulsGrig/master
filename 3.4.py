k = 0
n = 0
while n<3:
  from random import randint
  a = randint(0, 100)
  b = randint(0, 100)
  c = a + b
  print(a,'+',b,'=')
  d=int(input('Ответ:'))
  if d==c:
    print('Ответ правильный')
    k=k+1
  else:
    print('Ответ не правильный')
    n=n+1

print('Игра окончена . Правильных ответов :',k)