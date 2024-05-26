from PIL import Image
from module.tracer import getbg

image = Image.open("Test_Image/Test1.jpg")
mask = getbg(image)

mask = Image.save("./test.png")
