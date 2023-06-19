# How can I use tesseract OCR?
// plain

Tesseract OCR is an optical character recognition (OCR) engine that can be used to recognize text from images. It is an open-source software developed by Google and is available for free.

To use tesseract OCR, you need to install it on your system. You can install it using [pip](https://pypi.org/project/tesseract/) or [conda](https://anaconda.org/anaconda/tesseract).

Once installed, you can use the following example code to recognize text from an image:

```
from PIL import Image
import pytesseract

img = Image.open('example.png')
text = pytesseract.image_to_string(img)
print(text)
```

The output of the above code will be the text contained in the image.

The code consists of the following parts:
1.  `from PIL import Image` imports the Python Imaging Library (PIL) module which is used to open the image.
2. `import pytesseract` imports the Tesseract OCR library.
3. `img = Image.open('example.png')` opens the image file.
4. `text = pytesseract.image_to_string(img)` uses the Tesseract OCR library to recognize text from the image.
5. `print(text)` prints the recognized text.

For more information on using Tesseract OCR, you can refer to the [official documentation](https://tesseract-ocr.github.io/tessdoc/).

onelinerhub: [How can I use tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-1687146654)