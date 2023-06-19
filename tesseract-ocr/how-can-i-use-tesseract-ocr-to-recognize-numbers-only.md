# How can I use Tesseract OCR to recognize numbers only?
// plain

Tesseract OCR can be used to recognize numbers only by using the following steps:

1. Install Tesseract OCR on your local machine.
2. Create an image file containing only the numbers you want to recognize.
3. Run the following command to recognize the numbers in the image file:
```
tesseract <image-file> stdout -psm 7 digits
```
This will output the recognized numbers.

## Code explanation


* `tesseract`: This is the command used to run Tesseract OCR.
* `<image-file>`: This is the name of the image file containing the numbers to be recognized.
* `stdout`: This is used to specify that the output should be printed to the standard output.
* `-psm 7`: This is used to specify that only digits should be recognized.

## Helpful links

* [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract/wiki)
* [Tesseract OCR Installation Guide](https://github.com/tesseract-ocr/tesseract/wiki/Compiling#installation-guide)

onelinerhub: [How can I use Tesseract OCR to recognize numbers only?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-to-recognize-numbers-only)