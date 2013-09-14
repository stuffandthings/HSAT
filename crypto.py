from SimpleAES import SimpleAES

key = raw_input("Enter crypto password: ")
aes = SimpleAES(key)

# Encrypt
def encryptString(inputString):
	ciphertext = aes.encrypt(inputString)
	return ciphertext

# Decrypt
def decryptString(inputString):
	plaintext = aes.decrypt(inputString)
	return plaintext
