# How can I use Tesseract OCR in a GUI on Windows?
// plain

Using Tesseract OCR in a GUI on Windows is relatively simple. The following example code will demonstrate how to use the library:

```
#import libraries
import pytesseract
from PIL import Image

#get image
image = Image.open('example.png')

#run tesseract
text = pytesseract.image_to_string(image)

#print results
print(text)
```

The code above will read the text from an image file called 'example.png' and output it to the console.

The code consists of four parts:
1. Importing the necessary libraries.
2. Opening the image file.
3. Running Tesseract OCR on the image.
4. Printing the results.

## Helpful links

- [Pytesseract](https://pypi.org/project/pytesseract/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

onelinerhub: [How can I use Tesseract OCR in a GUI on Windows?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-in-a-gui-on-windows)