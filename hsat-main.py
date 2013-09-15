from readImageFile import *
from readTargetFile import *

imageList = initializeImage()
#RGBtupleList = createRGBList(imageList)
clearedList = clearLowestBits(imageList[2])

fileName = raw_input("Enter target filename: ")
fileList = constructFileList(fileName)

locationAndDataList = putDataInImage(clearedList, fileList, imageList)

imageSize = imageList[1]
createModifiedImage(locationAndDataList[3], imageSize)
