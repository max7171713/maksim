from PIL import Image
x = Image.open("bghsg.png")
c = x.crop((0,50,150,200))
c.save("bghsg.png")
x.close()