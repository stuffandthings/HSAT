import Image
from readTargetFile.py import *

def initializeImage():
	imageName = raw_input("Please enter image file name: ")
	img = Image.open(imageName)
	imageFile = img.load()
	imageSize = img.size
	imageList = []
	imageList.append(imageName)
	imageList.append(imageSize)
	imageList.append(imageFile)
	return imageList

def canHideImage(imageList, fileList):
	if imageList[1][0]*imageList[1][1] < fileList[1]:
		print "Data too big to hide in image."
		return false
	else:
		return true

def createRGBList(imageList):
	RGBtupleList = []
	for i in range(0, imageList[1][0]):
		for j in range(0, imageList[1][1]):
			RGBtupleList.append(imageList[2][i][j])
	return RGBtupleList

def clearLowestBits(RGBtupleList):
	clearedList = []
	for i in range(len(RGBtupleList)):
		tempTuple = (0,0,0)
		for j in range(3):
			temp = "{0:08b}".format(RGBtupleList[i][j])
			tempCleared = temp & 11111100
			tempTuple[j] = tempCleared
		clearedList.append(tempTuple)
	return clearedList

def putDataInImage(RGBlist, fileList, imageList):
	modifiedImageTupleList = []
	
	imageSize = imageList[1] #this is a tuple
	2bitChunkListLength = len(fileList[2])
	formatBinary = fileList[0]		
	lengthBinary = fileList[1]
	dataBinary = fileList[2]
	
	if (len(formatBinary) + len(lengthBinary) + 2bitChunkListLength) > 6*len(RGBlist):
		print "Too much data. Try larger image."

	pixelCounter = 0
	
	index = 0
	while index < len(formatBinary):
		tempTuple = (0, 0, 0)
		for j in range(3):
			temp = RGBlist[pixelCounter][j] | "{0:0>8}".format(formatBinary[index])
			tempTuple[j] = temp
			index += 1
		modifiedImageTupleList.append(tempTuple)			
		pixelCounter += 1
	
	formatEndLocation = pixelCounter	

	index2 = 0
	while index2 < len(lengthBinary):
		tempTuple = (0, 0, 0)
		for j in range(3):
			temp = RGBlist[pixelCounter][j] | "{0:0>8}".format(lengthBinary[index2])
			tempTuple[j] = temp
			index2 += 1
		modifiedImageTupleList.append(tempTuple)
		pixelCounter += 1

	lengthEndLocation = pixelCounter

	index3 = 0
	while index3 < 2bitChunkListLength:
		tempTuple = (0, 0, 0)
		for j in range(3):
			temp = RGBlist[pixelCounter][j] | "{0:0>8}".format(dataBinary[index3])
			tempTuple[j] = temp
			index3 += 1
		modifiedImageTupleList.append(tempTuple)
		pixelCounter += 1

	dataEndLocation = pixelCounter
	
def createModifiedImage(tupleList, imageSize):
	modifiedImage = Image.new(RGB, imageSize)
	modifiedImage.putdata(tupleList)
	modifiedImage.save("ModifiedImage.jpg")
	print "New image with hidden encrypted data saved as 'ModifiedImage.jpg'"
	
	
