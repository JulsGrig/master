from PIL import Image
file = "др.jpg"

with Image.open(file) as img:
    img.load()
img_obr=img.crop((0,0,900,900))
img.show()
img_obr.show()