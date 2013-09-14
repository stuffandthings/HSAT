import Image

imageName = raw_input("Please enter image file name: ")

im = Image.open(imageName)
imageFile = im.load()
imageSize = im.size

print im.getpixel((10, 10))

#for  width in range(0, imageSize[0]):
#	for height in range(0, imageSize[1]):
#		print imageFile[width, height]
