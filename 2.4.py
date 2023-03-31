color1 = input ('Первый цвет: ')
color2 = input('Второй цвет: ')
colors = ['красный' , 'синий','желтый']
itog = 'Не верно введены цвета'
if color1 in colors and color2 in colors:
   if color1 == colors [0]:
      if color2 == colors [1]:
        itog = 'фиолетовый'
      elif color2 == colors [2]:
        itog = 'оранжевый'
      else:
        itog=color1
if color1 == colors[1]:
   if color2==colors[0]:
       itog='фиолетовый'
   elif color2 == colors [2]:
       itog='зеленый'
   else:
       itog=color1
if color1 == colors[2]:
   if color2 == colors[0]:
       itog = 'фиолетовый'
   elif color2 == colors[1]:
       itog = 'зеленый'
   else:
       itog = color1
print(itog)
