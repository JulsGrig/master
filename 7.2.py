from PIL import Image
filename = "a46b2bbcc6475ac0bd33e55e426da996-3.jpg"
with Image.open(filename) as img:
    img.load()
one_img= img.resize((img.width//3,img.height//3))
one_img.save("new.jpg")
one_img.show()
two_img=img.rotate(90)
two_img.save("new2.jpg")
two_img.show()
three_img=img.rotate(270)
three_img.save("new3.jpg")
three_img.show()