# How can I use Tesseract OCR?
// plain

Tesseract OCR is an open source Optical Character Recognition (OCR) engine developed by Google. It can be used to recognize text from images, such as scanned documents and photos.

Here is an example of how to use Tesseract OCR to recognize text from an image:

```python
# import the necessary packages
from PIL import Image
import pytesseract

# load the image
image = Image.open("example.png")

# run tesseract OCR
text = pytesseract.image_to_string(image)

# display the OCR result
print(text)
```

The output of the above code is:
```
This is an example of OCR text recognition.
```

## Code explanation

- `from PIL import Image`: imports the Python Imaging Library (PIL) package, which is used to load the image.
- `import pytesseract`: imports the pytesseract package, which is used to run Tesseract OCR.
- `image = Image.open("example.png")`: loads the image from the file `example.png`.
- `text = pytesseract.image_to_string(image)`: runs Tesseract OCR on the image.
- `print(text)`: prints the OCR result.

## Helpful links
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Python Imaging Library (PIL)](https://pillow.readthedocs.io/en/stable/)
- [pytesseract](https://pypi.org/project/pytesseract/)

onelinerhub: [How can I use Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr)