from PIL import Image
filename = "др.jpg"

with Image.open(filename) as img:
    img.load()
img_obr=img.crop((0,0,900,900))
img.show()
img_obr.show()