Hide Stuff And Things (HSAT for short) is a Steganography tool implemented in Python 2.7.6.

What is Steganography?
From the Wikipedia page, Steganography "is the art or practice of concealing a message, image, or file within another message, image, or file." Steganography has a pretty cool history. Read more about it here: http://en.wikipedia.org/wiki/Steganography

What are the capabilities of this tool?
HSAT is currently capable of hiding a string message in an image and also retrieving this message, given the modified image.
The goal is to allow the user to take any image and any file, and be able to hide the file inside the image. The method splits up binary data and hides it in the least significant bits of each color value in each pixel of the image.

What are the limitations of this tool?
The current implementation only allows for a text secret message to be hidden inside the image. There are complications with handling different file formats (e.g. troublesome to get a pdf file split into binary, hidden inside the image, and be able to extract the data from the image and convert it back into a pdf file)

What features still need to be implemented?
- Store a sort of file signature header in the first row of the image that includes information of the filetype etc.
- Add the ability of encrypt the data before embeddeding it in the image. (and ofcourse... the ability to decrypt the message)
- GUI
- Better algorithms can surely be implemented (i.e. data gets embedded in sequential order, creating a very distinct pattern that is visible in the image, making it more obvious that there is a message hidden inside the image)

Feel free to use/reuse my code.
