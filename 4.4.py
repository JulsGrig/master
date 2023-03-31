a=input('Введите номер билета')
x=0
y=0
if len(a)%2==0 :
   for i in a[0:int(len(a)/2)]:
       x=x+int(i)
   for i in a[int(len(a)/2):int(len(a))+1]:
       y=y+int(i)
   if x==y:
     print('счастливый билет')
   else:
     print(' не счастливый билет')