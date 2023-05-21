from PIL import Image, ImageDraw, ImageFont
name = input("Введите имя получателя: ")
filename = "др.jpg"
with Image.open(filename) as img:
   img.load()
font= ImageFont.truetype("arial.ttf", 55)
draw = ImageDraw.Draw(img)
draw_text = ImageDraw.Draw(img)
draw_text.text(
    (100, 100),
    "Dear,"+ name,
    font = font,
    fill='#1C0606')
img.show()