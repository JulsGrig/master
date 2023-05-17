from PIL import Image
filename = "a46b2bbcc6475ac0bd33e55e426da996-3.jpg"
with Image.open(filename) as img:
    img.load()

img.show()
a,b=img.size
c=img.format
d=img.mode
print("Ширина: ",a)
print("Высота: ",b)
print("Формат: ",c)
print("Цветовая модель: ",d)
