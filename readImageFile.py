import Image

imageName = raw_input("Please enter image file name: ")

image = Image.open(imageName)
imageFile = im.load()
imageSize = im.size

print im.getpixel((10, 10))[0]

