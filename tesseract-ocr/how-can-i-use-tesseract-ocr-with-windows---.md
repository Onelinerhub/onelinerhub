# How can I use Tesseract OCR with Windows 10?
// plain

Tesseract OCR can be used with Windows 10 in the following way:

1. Install the Tesseract OCR executable from [this link](https://github.com/UB-Mannheim/tesseract/wiki).
2. Install the language data from [this link](https://github.com/tesseract-ocr/tessdata).
3. Create a Python script to read the image file and pass it to Tesseract OCR.

## Example code

```
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"<path to tesseract executable>"

img = Image.open('<path to image file>')
text = pytesseract.image_to_string(img)

print(text)
```

Output (if any):
The text extracted from the image.

## Code explanation

- `import pytesseract`: imports the pytesseract module which provides an interface to the Tesseract OCR engine.
- `from PIL import Image`: imports the Python Imaging Library (PIL) module which provides functions to open, manipulate and save images.
- `pytesseract.pytesseract.tesseract_cmd = r"<path to tesseract executable>"`: sets the path to the Tesseract OCR executable.
- `img = Image.open('<path to image file>')`: opens the image file.
- `text = pytesseract.image_to_string(img)`: passes the image to Tesseract OCR and extracts the text from it.
- `print(text)`: prints the extracted text.

onelinerhub: [How can I use Tesseract OCR with Windows 10?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-with-windows---)