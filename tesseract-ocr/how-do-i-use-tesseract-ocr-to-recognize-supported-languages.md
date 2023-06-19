# How do I use tesseract OCR to recognize supported languages?
// plain

Tesseract OCR is an open source optical character recognition (OCR) engine. It can be used to recognize text in over 100 languages.

To use tesseract OCR to recognize supported languages, you need to install the tesseract command line tool. After installation, you can use the `tesseract` command to recognize text in different languages.

For example, to recognize text in Spanish, you can use the following command:

```
tesseract image.png stdout -l spa
```

The output of the command will be the recognized text in Spanish.

## Code explanation


* `tesseract` - the command line tool for tesseract OCR
* `image.png` - the image file containing the text to be recognized
* `stdout` - the output of the command will be printed to the standard output
* `-l spa` - the language parameter, `spa` stands for Spanish

For more information about tesseract OCR, please refer to the [official documentation](https://github.com/tesseract-ocr/tesseract/wiki).

onelinerhub: [How do I use tesseract OCR to recognize supported languages?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-to-recognize-supported-languages)