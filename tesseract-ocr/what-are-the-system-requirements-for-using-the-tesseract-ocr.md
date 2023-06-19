# What are the system requirements for using the Tesseract OCR?
// plain

The Tesseract OCR system requires the following system requirements:

1. Python 3.5+: Tesseract OCR is compatible with Python 3.5 and later.

2. Leptonica library: Tesseract OCR requires the Leptonica library for image manipulation.

3. Tesseract v4.0+: Tesseract OCR requires version 4.0 or higher of the Tesseract library.

4. ImageMagick: Tesseract OCR requires the ImageMagick library for image manipulation.

5. Operating System: Tesseract OCR is supported on Windows, MacOS, and Linux.

## Example code

```
import pytesseract
from PIL import Image

img = Image.open('example.jpg')
text = pytesseract.image_to_string(img)
print(text)
```

## Output example

```
This is an example of text.
```

## Helpful links

- [Python 3.5+](https://www.python.org/downloads/)
- [Leptonica Library](http://www.leptonica.com/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [ImageMagick](https://imagemagick.org/index.php)

onelinerhub: [What are the system requirements for using the Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/what-are-the-system-requirements-for-using-the-tesseract-ocr)