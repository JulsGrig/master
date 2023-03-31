k=int(input('Введите кол-во слов:'))
s =''
for i in range(k):
  word = input('Введите слово: ')
  s = s + word + ' '
print(s)