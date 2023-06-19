# How can I use Tesseract OCR to get the position of text?
// plain

Tesseract OCR is an open source optical character recognition (OCR) engine. It can be used to identify and extract text from images. To get the position of text using Tesseract OCR, you need to use the `GetBoundingBoxText` function. This function takes an image as an input and returns the coordinates of the bounding box of each character in the text.

## Example code

```
import pytesseract
from PIL import Image

# Load image
img = Image.open('image.png')

# Get position of text
position = pytesseract.image_to_boxes(img)

# Print position of text
print(position)
```

## Output example

```
h 10 11 0 1
e 12 11 0 1
l 14 11 0 1
l 16 11 0 1
o 18 11 0 1
```

The code above loads an image and uses the `image_to_boxes` function to get the position of the text in the image. The output is a list of characters and their coordinates.

The code consists of the following parts:

- `import pytesseract`: imports the Tesseract OCR library.
- `from PIL import Image`: imports the Python Imaging Library (PIL) library.
- `img = Image.open('image.png')`: loads the image.
- `position = pytesseract.image_to_boxes(img)`: uses the `image_to_boxes` function to get the position of the text in the image.
- `print(position)`: prints the position of the text.

## Helpful links

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Python Imaging Library (PIL)](https://pillow.readthedocs.io/en/stable/)

onelinerhub: [How can I use Tesseract OCR to get the position of text?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-to-get-the-position-of-text)