# How can I use Tesseract OCR to recognize only numbers?
// plain

Tesseract OCR is an open source optical character recognition (OCR) engine that can be used to recognize only numbers. It can be used to read text from images, and it can be trained to recognize only numbers.

To use Tesseract OCR to recognize only numbers, you will need to install the Tesseract OCR engine and setup the environment for it.

Once the environment is setup, you can use the following code to recognize only numbers from an image:

```
from PIL import Image
import pytesseract

# Read image from which text needs to be extracted
img = Image.open('image.png')

# Recognize only numbers
text = pytesseract.image_to_string(img, config='--psm 6')

# Print recognized text
print(text)
```

This will output the text recognized from the image, which will only include numbers.

## Code explanation

1. `from PIL import Image`: This imports the Image module from the Python Imaging Library (PIL) which is used to open the image file.
2. `import pytesseract`: This imports the pytesseract module which provides the interface for using Tesseract OCR.
3. `img = Image.open('image.png')`: This opens the image file that needs to be read.
4. `text = pytesseract.image_to_string(img, config='--psm 6')`: This uses the pytesseract module to read the text from the image, and the `--psm 6` parameter is used to specify that only numbers should be recognized.
5. `print(text)`: This prints the output of the recognized text.

## Helpful links
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Python Imaging Library (PIL)](https://pillow.readthedocs.io/en/stable/)
- [Pytesseract](https://pypi.org/project/pytesseract/)

onelinerhub: [How can I use Tesseract OCR to recognize only numbers?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-to-recognize-only-numbers)