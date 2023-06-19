# How can I use Python to get the coordinates of words detected by Tesseract OCR?
// plain

The Tesseract OCR library has a Python wrapper that can be used to get the coordinates of words detected by Tesseract OCR. The `pytesseract` library provides a method `image_to_data` which can be used to get the coordinates of the words detected by Tesseract OCR.

## Example code

```
import pytesseract
from PIL import Image

# Read the image
img = Image.open('image.png')

# Get the word coordinates
data = pytesseract.image_to_data(img)
print(data)
```

## Output example

```
level	page_num	block_num	par_num	line_num	word_num	left	top	width	height	conf	text
1	1	0	0	0	0	0	0	0	0	-1
2	1	1	0	0	0	162	51	622	66	-1
3	1	1	1	0	0	162	51	622	66	95
4	1	1	1	1	0	162	51	44	66	95	This
4	1	1	1	1	1	212	51	90	66	95	is
4	1	1	1	1	2	312	51	52	66	95	a
4	1	1	1	1	3	372	51	81	66	95	test
4	1	1	1	1	4	468	51	53	66	95	image
```

The output contains the coordinates for each word detected. The `left` and `top` columns contain the x and y coordinates of the top left corner of the word, respectively. The `width` and `height` columns contain the width and height of the word, respectively.

## Code explanation

- `import pytesseract`: imports the `pytesseract` library
- `from PIL import Image`: imports the `Image` class from the `PIL` library
- `img = Image.open('image.png')`: reads the image
- `data = pytesseract.image_to_data(img)`: gets the coordinates of the words detected by Tesseract OCR
- `print(data)`: prints the coordinates of the words detected

## Helpful links
- [pytesseract documentation](https://pypi.org/project/pytesseract/)
- [Pillow documentation](https://pillow.readthedocs.io/en/stable/)

onelinerhub: [How can I use Python to get the coordinates of words detected by Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-python-to-get-the-coordinates-of-words-detected-by-tesseract-ocr)