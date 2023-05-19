import ImageFilter
from PIL import Image
filename = "a46b2bbcc6475ac0bd33e55e426da996-3.jpg"
with Image.open(filename) as img:
    img.load()

one_img= img.filter(ImageFilter.FIND_EDGES)
one_img.save("new1f.jpg")
one_img.show()

two_img=img.filter(ImageFilter.CONTOUR)
two_img.save("new2f.jpg")
two_img.show()

three_img=img.filter(ImageFilter.EDGE_ENHANCE)
three_img.save("new3f.jpg")
three_img.show()

four_img=img.filter(ImageFilter.EMBOSS)
four_img.save("new4f.jpg")
four_img.show()

five_img=img.filter(ImageFilter.SHARPEN)
five_img.save("new5f.jpg")
five_img.show()