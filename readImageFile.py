import Image
#from readTargetFile.py import *

def initializeImage():
	imageName = raw_input("Please enter image file name: ")
	img = Image.open(imageName)
	#imageFile = img.load()
	imageFile = list(img.getdata())
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
	for i in range(0, imageList[1][0]-1):
		for j in range(0, imageList[1][1]-1):
			#tuple = (i, j)
			print i, j
			tmp = imageList[2]
			RGBtupleList.append(tmp[i][j])
	return RGBtupleList

def clearLowestBits(RGBtupleList):
	clearedList = []
	for i in range(len(RGBtupleList)):
		tempList = []
		for j in range(3):
			#temp = "{0:08b}".format(RGBtupleList[i][j])
			temp = RGBtupleList[i][j]
			tempCleared = temp & 0b11111100
			#tempClearedNo0b = "{0:08b}".format(tempCleared)
			tempList.append(tempCleared)
			#tempTuple[j] = tempCleared
		clearedList.append(tuple(tempList))
	return clearedList

def putDataInImage(RGBlist, fileList, imageList):
	modifiedImageTupleList = []
	
	imageSize = imageList[1] #this is a tuple
	dataList = fileList[2]
	dataListLen = len(dataList)
	formatBinary = fileList[0]		
	lengthBinary = fileList[1]
	dataBinary = fileList[2]
	
	if (len(formatBinary) + len(lengthBinary) + dataListLen) > 6*len(RGBlist):
		print "Too much data. Try larger image."

	pixelCounter = 0
	print formatBinary
	index = 1
	while index < len(formatBinary):
		tempTuple = (0, 0, 0)
		for j in range(3):
			#print formatBinary[index]
			print RGBlist[pixelCounter][j]
			temp = RGBlist[pixelCounter][j] | "{0:08b}".format(formatBinary[index])
			tempTuple[j] = temp
			index += 1
		modifiedImageTupleList.append(tempTuple)			
		pixelCounter += 1
	
	formatEndLocation = pixelCounter	

	index2 = 0
	while index2 < len(lengthBinary):
		tempTuple = (0, 0, 0)
		for j in range(3):
			temp = RGBlist[pixelCounter][j] | "{0:08b}".format(lengthBinary[index2])
			tempTuple[j] = temp
			index2 += 1
		modifiedImageTupleList.append(tempTuple)
		pixelCounter += 1

	lengthEndLocation = pixelCounter

	index3 = 0
	while index3 < dataListLen:
		tempTuple = (0, 0, 0)
		for j in range(3):
			temp = RGBlist[pixelCounter][j] | "{0:08b}".format(dataBinary[index3])
			tempTuple[j] = temp
			index3 += 1
		modifiedImageTupleList.append(tempTuple)
		pixelCounter += 1

	dataEndLocation = pixelCounter
	
        locationAndDataList = []
	locationAndDataList.append(formatEndLocation)
	locationAndDataList.append(lengthEndLocation)
	locationAndDataList.append(dataEndLocation)
	locationAndDataList.append(modifiedImageTupleList)

	return locationAndDataList
	
def createModifiedImage(tupleList, imageSize):
	modifiedImage = Image.new(RGB, imageSize)
	modifiedImage.putdata(tupleList)
	modifiedImage.save("ModifiedImage.jpg")
	print "New image with hidden encrypted data saved as 'ModifiedImage.jpg'"
	
	
