# How do I use the Tesseract OCR API?
// plain

The Tesseract OCR API is an open-source library that can be used to recognize text from an image. To use the Tesseract OCR API, you will need to install it on your computer.

Once the Tesseract OCR API is installed, you can use the following code example to recognize text from an image:

```
import pytesseract
from PIL import Image

# Read image from which text needs to be extracted
img = Image.open('sample.png')

# Run tesseract OCR on image
text = pytesseract.image_to_string(img)

# Print recognized text
print(text)
```

The code example above will print out the text that is recognized from the image.

## Code explanation


- `import pytesseract`: This imports the Tesseract OCR API library.
- `from PIL import Image`: This imports the Python Imaging Library (PIL) which is used to read images.
- `img = Image.open('sample.png')`: This reads an image file called ‘sample.png’.
- `text = pytesseract.image_to_string(img)`: This uses the Tesseract OCR API to recognize text from the image.
- `print(text)`: This prints out the text that is recognized from the image.

## Helpful links
- [Tesseract OCR API Documentation](https://github.com/tesseract-ocr/tesseract/wiki)
- [Python Imaging Library (PIL)](https://pillow.readthedocs.io/en/stable/index.html)

onelinerhub: [How do I use the Tesseract OCR API?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-the-tesseract-ocr-api)