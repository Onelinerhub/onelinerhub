# How can I install and use Tesseract OCR on Fedora?
// plain

To install and use Tesseract OCR on Fedora, you can follow these steps:

1. Install the Tesseract OCR package by running the command: `dnf install tesseract`.

2. To test the installation, you can run the command: `tesseract -v` which should output the version of Tesseract OCR installed.

3. To convert an image to text, use the command `tesseract <image-file> <output-file>`. For example, `tesseract sample.png output.txt`

4. To specify the language of the text in the image, add the `-l` option followed by the language code. For example, `tesseract sample.png output.txt -l eng`

5. To get a list of available language codes, use the command `tesseract --list-langs`

6. To get more information about Tesseract OCR, refer to the [official documentation](https://tesseract-ocr.github.io/tessdoc/Home.html).

7. To get help with specific commands, use the `-h` option. For example, `tesseract -h`

onelinerhub: [How can I install and use Tesseract OCR on Fedora?](https://onelinerhub.com/tesseract-ocr/how-can-i-install-and-use-tesseract-ocr-on-fedora)