from PIL import Image
a= {1:"нг.jpg", 2 :"свадьба.jpg" ,3 : "пасха.jpg" ,4:"мама.png" ,5:"др.jpg"}
print("1-Новый год, 2- День свадьбы,3-Пасха, 4-День матери,5-День рождения")
b=int(input("Введите номер праздника:"))
filename=a[b]
with Image.open(filename) as img:
    img.load()
img.show()

