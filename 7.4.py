from PIL import Image
water = "banana.png"
with Image.open (water) as img_water:
   img_water.load()
img_water = Image.open(water)
img_water = img_water.resize((img_water.width // 10, img_water. height // 10))
filename ="a46b2bbcc6475ac0bd33e55e426da996-3.jpg"
with Image. open (filename) as img:
   img.load ()
img.paste(img_water, (420, 500), img_water)
img.save ("watermark.png")
img.show()
