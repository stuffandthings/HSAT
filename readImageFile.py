import Image

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

def putDataInImage(RGBlist, fileList):
	

def createModifiedImage(tupleList, imageSize):
	modifiedImage = Image.new(RGB, imageSize)
	modifiedImage.putdata(tupleList)
	modifiedImage.save("ModifiedImage.jpg")
	
