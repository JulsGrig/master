word=input('Введите слово:')
point={"авеинорст": 1,"дклмпу": 2,"бгёья": 3,"йы": 4,"жзхцч": 5,"шею": 8,"фщь":10 }
S = 0
for i in word:
   for key , value in point.items():
      if i in key:
          S += value

print('Сумма',S)
