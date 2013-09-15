import binascii
from crypto import *

# Asks user for target filename (.format should be included)
fileName = raw_input("Enter target filename: ")

# Stores the file format from filename, hi.pdf... fileFormat will store pdf
fileFormat = fileName.split(".")[1] 

# Opens the file, stores all file data in variable fileData
inputFile = open(fileName)
fileData = inputFile.read()
encryptedData = encryptString(fileData)

# Gets the length of the data in the file
fileLength = len(fileData)

# New list to store format, length, and data
fileList = []

def stringToBin(string):
	return bin(int(binascii.hexlify(string), 16))

def binToString(binaryString):
	return binascii.unhexlify('%x' % int(binaryString, 2))

def constructFileList(fileName):
	
	binaryEncryptedData = stringToBin(encryptedData)
	binaryFileFormat = stringToBin(fileFormat)	
	dataLength = len(binaryEncryptedData)

	splitFormat = []
	for x in range(0, len(binaryFileFormat), 2):
		splitFormat.append(binaryFileFormat[x:x+2]
	
	splitLength = []
	for x in range(0, len(binaryEncryptedData), 2):
		splitLength.append(bin(dataLength)[2:][x:x+2])

	splitDataList = []
	for x in range(0, dataLength, 2):
		splitDataList.append(binaryEncryptedData[x:x+2])
	
	fileList.append(splitFormat)
	fileList.append(splitLength)
	fileList.append(splitDataList) # fileList[2] gives data (string)
	
	return fileList

