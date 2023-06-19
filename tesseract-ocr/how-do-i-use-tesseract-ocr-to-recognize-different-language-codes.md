# How do I use tesseract OCR to recognize different language codes?
// plain

Tesseract OCR is an open-source optical character recognition (OCR) engine that can be used to recognize different language codes. It is written in C++ and supports multiple languages. To use it, you need to install the Tesseract OCR package on your system.

To recognize different language codes with Tesseract OCR, you need to specify the language code while initializing the engine. The language codes can be found in the Tesseract documentation.

For example, the following code snippet initializes the Tesseract engine with the French language code and performs OCR on an image:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"<path_to_tesseract_executable>"

text = pytesseract.image_to_string(image, lang="fra")
print(text)
```

The output of the above code will be the OCR result of the image in French.

## Code explanation

- `pytesseract.pytesseract.tesseract_cmd = r"<path_to_tesseract_executable>"`: This line sets the path to the Tesseract executable.
- `lang="fra"`: This specifies the French language code for the Tesseract engine.
- `pytesseract.image_to_string(image, lang="fra")`: This performs OCR on the image using the French language code.

## Helpful links
- [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract/wiki)
- [PyTesseract Documentation](https://pypi.org/project/pytesseract/)

onelinerhub: [How do I use tesseract OCR to recognize different language codes?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-to-recognize-different-language-codes)