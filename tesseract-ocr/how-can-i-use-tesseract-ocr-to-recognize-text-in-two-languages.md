# How can I use Tesseract OCR to recognize text in two languages?
// plain

Tesseract OCR is an open-source optical character recognition (OCR) engine that can be used to recognize text in two languages. It uses a combination of a library of trained language-specific data files and an adaptive recognition engine to identify text in a variety of languages.

To use Tesseract OCR to recognize text in two languages, you will need to install the Tesseract OCR engine and the language-specific data files for the two languages you wish to use. The language-specific data files can be downloaded from the [Tesseract OCR GitHub repository](https://github.com/tesseract-ocr/tessdata).

Once the Tesseract OCR engine and language-specific data files are installed, you can use the following example code to recognize text in two languages:

```python
from tesserocr import PyTessBaseAPI

# Create Tesseract OCR API object
api = PyTessBaseAPI()

# Set language to recognize
api.SetVariable('tessedit_char_whitelist', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
api.SetVariable('language_1', 'eng')
api.SetVariable('language_2', 'fra')

# Initialize Tesseract OCR engine
api.Init('.', 'eng+fra')

# Recognize text in two languages
text_1 = api.GetUTF8Text()
text_2 = api.GetUTF8Text()

# Print recognized text
print(text_1)
print(text_2)
```

The code above will recognize text in two languages, `eng` and `fra`, and print the recognized text to the console.

The code consists of the following parts:

1. Create a `PyTessBaseAPI` object: This creates an object of the Tesseract OCR API.
2. Set language to recognize: This sets the language-specific data files to be used for recognition.
3. Initialize Tesseract OCR engine: This initializes the Tesseract OCR engine with the language-specific data files.
4. Recognize text in two languages: This recognizes text in two languages, `eng` and `fra`, and stores the recognized text in two variables.
5. Print recognized text: This prints the recognized text to the console.

For more information about using Tesseract OCR to recognize text in two languages, see the [Tesseract OCR documentation](https://github.com/tesseract-ocr/tesseract/wiki).

onelinerhub: [How can I use Tesseract OCR to recognize text in two languages?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-to-recognize-text-in-two-languages)