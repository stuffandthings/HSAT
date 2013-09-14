# Asks user for target filename (.format should be included)
fileName = raw_input("Enter target filename: ")

# Stores the file format from filename, hi.pdf... fileFormat will store pdf
fileFormat = fileName.split(".")[1] 

# Opens the file, stores all file data in variable fileData
inputFile = open(fileName)
fileData = inputFile.read()

# Gets the length of the data in the file
fileLength = len(fileData)

# New list to store format, length, and data
fileList = []

def constructFileList(fileName):
	fileList.append(fileFormat)
	fileList.append(fileLength)
	fileList.append(fileData)
	return fileList

print constructFileList(fileName)
