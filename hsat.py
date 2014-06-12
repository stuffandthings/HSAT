import binascii #binascii for string > binary and binary > string methods.
from PIL import Image #PILLOW, fork of PIL. Python Imaging Library.

class image:
	def __init__(self, imageName):
		self.img = Image.open(imageName)
		self.imgLoc = imageName
		self.imgSize = self.img.size
		self.imgData = list(self.img.getdata())
		
	#Clear lowest two bits from each pixel color value
	#e.g. '0b11111111' becomes '0b11111100'
	def clearBits(self):
		tmpData = []
		for tuple in self.imgData:
			x,y,z = tuple[0],tuple[1],tuple[2]
			tmpTuple = (x & (x-3),y & (y-3),z & (z-3))
			tmpData.append(tmpTuple)
		self.imgData = tmpData
		self.img = self.img.putdata(tmpData)
	
	#Given a RGB tuple list, data, create a new image.
	#data looks like [(100,255,255),(15,15,20),...]	
	def modifyImage(self, data):
		tmp = Image.new('RGB', self.imgSize)
		tmp.putdata(data)
		tmp.save('ModifiedImage.png')
		return image('ModifiedImage.png')
	
	#Given a list of split data, hides data in lowest two bits and saves a modified image.
	#e.g. if RGB values of a pixel in the original image are (255,255,255)
	#     the lowest two bits are cleared, so 255 is 0b11111111 which becomes 0b11111100
	#     now if one element of the split data list is '0b01', the new pixel color
	#     value becomes 0b11111101.
	def insertData(self, l , counter=-1):
		flattened, tmpData, i = list(sum(self.imgData, ())), [], 0
		while len(l) > abs(counter):
			flattened[counter] = flattened[counter] | int(l[abs(counter+1)],2)
			counter -= 1
		while i < len(flattened):
			tmp = tuple(flattened[i:i+3])
			tmpData.append(tmp)
			i += 3
		return tmpData
		
	#Extracts data from an image. Gets a list of all the last two digits
	#
	def extractData(self, counter=0):
		flattened, tmpData = list(sum(self.imgData, ())), []
		for x in flattened:
			tmp = bin(x)[8:]
			tmpData.append(tmp)
		return tmpData
		#return binascii.unhexlify('%x' % int('0b'+''.join(tmpData), 2))
	
class secret:
	def __init__(self, s):
		#Multipurpose secret class. Provisions for binary and regular strings. 
		#Minor convenience for both forward and backward directions of process.
		if (s[:2] != '0b') & (type(s) != list):
			self.msg = s
			self.msgBinary = bin(int(binascii.hexlify(s), 16))
			self.msgBinaryLen = len(self.msgBinary)-2
		elif type(s) == list:
			self.msgBinaryLen = (2*(len(s)-1))+len(str(s[len(s)-1]))-2
			self.msgBinary = '0b'+self.joinMsg(s)
			self.msg = binascii.unhexlify('%x' % int(self.msgBinary, 2))
		else:
			self.msgBinary = s
			self.msgBinaryLen = len(s)-2
			self.msg = c
		
	#splits the binary string into chunks of two
	#e.g. '0b11010111' becomes ['0b11','0b01','0b01','0b11']
	#NOTE: this method keeps the '0b' python binary string formatting.
	def splitMsg(self):
		tmp, i = [], 2
		while (i < self.msgBinaryLen):
			tmp.append('0b'+self.msgBinary[i:i+2])
			i += 2
		tmp.append('0b'+self.msgBinary[i:])
		return tmp
		
	#joins a split binary string list into a unified binary string
	#e.g. ['0b11','0b01','0b01','0b11'] becomes '0b11010111'
	#NOTE: this method ensures the 0b in front of the binary string
	#      which is how python formats binary strings.
	def joinMsg(self, l, counter=0):
		msg = ''
		while counter < len(l):
			msg = msg+l[counter][2:]
		return msg
		
#header class to store meta-data of secret.
#i.e. if secret is a pdf, header will store that information.
class header:
	def __init__(self, image, secret):
		self.binLen = secret.msgBinaryLen
		self.head = "len="+str(self.binLen)
		self.headerBin = bin(int(binascii.hexlify(self.head), 16))
		self.headerBinLen = len(self.headerBin)
	
	def splitHeader(self):
		tmp, i = [], 2
		while (i < self.headerBinLen):
			tmp.append('0b'+self.headerBin[i:i+2])
			i += 2
		return tmp
		
def main():
	#fileName = raw_input("Image file name:\n")
	#img = image(fileName)
	img = image('img.png')
	img.clearBits()
	sec = secret(raw_input('Secret:\n'))
	secData = sec.splitMsg()
	#print secData
	img2 = img.modifyImage(img.insertData(secData))
	wee = img2.extractData()
	#print wee
	print img.imgData[-1]
	print img2.imgData[-1]
	
main()