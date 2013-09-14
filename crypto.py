from SimpleAES import SimpleAES

# Encrypt
def encryptString(inputString):
	key = raw_input("Enter crypto password: ")
	aes = SimpleAES(key)
	ciphertext = aes.encrypt(inputString)
	return ciphertext

# Decrypt
def decryptString(inputString):
	key = raw_input("Enter crypto password: ")
	aes = SimpleAES(key)
	plaintext = aes.decrypt(inputString)
	return plaintext
