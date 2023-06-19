# How can I use Tesseract OCR on Windows via the command line?
// plain

Tesseract OCR is an open source Optical Character Recognition (OCR) engine that can be used to extract text from images. It can be used on Windows via the command line by following these steps:

1. Download and install [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) for Windows.
2. Open the command line and navigate to the directory where the Tesseract executable is located.
3. Use the command `tesseract <input image> <output file>` to recognize text from an image and save it to a text file. For example:
```
tesseract image.png output.txt
```
4. The recognized text will be saved to the output file.
5. Optionally, you can use the `-l` option to specify a language for Tesseract to use. For example:
```
tesseract image.png output.txt -l eng
```
6. You can also use the `-psm` option to specify a page segmentation mode. For example:
```
tesseract image.png output.txt -psm 6
```
7. For more options, you can refer to the [Tesseract documentation](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html).

onelinerhub: [How can I use Tesseract OCR on Windows via the command line?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-on-windows-via-the-command-line)