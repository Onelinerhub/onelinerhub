# How do I find the official website for Tesseract OCR?
// plain

The official website for Tesseract OCR is [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract).

The website provides the source code for Tesseract OCR as well as other resources such as documentation, tutorials, and a discussion forum.

The website also provides links to other Tesseract OCR-related projects, such as:

- [Tesseract-OCR-iOS](https://github.com/gali8/Tesseract-OCR-iOS): An open-source iOS framework for Tesseract OCR
- [pytesseract](https://github.com/madmaze/pytesseract): A Python wrapper for Tesseract OCR
- [Tesseract-Android-Tools](https://github.com/rmtheis/tess-two): A collection of tools for Tesseract OCR on Android

In addition, the website provides links to download the Tesseract OCR binaries for various platforms, such as Windows, macOS, and Linux.

The website also contains example code for using Tesseract OCR in various programming languages, such as Python:

```python
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('example.png')
text = pytesseract.image_to_string(img)
print(text)
```

## Output example

```
This is an example of text
```

onelinerhub: [How do I find the official website for Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-find-the-official-website-for-tesseract-ocr)