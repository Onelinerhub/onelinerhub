# How can I use Tesseract OCR on Ubuntu 20.04?
// plain

Tesseract OCR is an open source optical character recognition (OCR) engine for Ubuntu 20.04. It can be used to recognize text in images and convert them into editable text.

To install Tesseract OCR on Ubuntu 20.04, open a terminal and run the following command:

```
sudo apt-get install tesseract-ocr
```

Once installed, you can use Tesseract OCR by running the following command:

```
tesseract <image_file> <output_file>
```

For example, to recognize text from an image `example.png` and save the output in `example.txt`, run the following command:

```
tesseract example.png example.txt
```

The output file `example.txt` will contain the recognized text from the image.

You can also use Tesseract OCR to recognize text from a PDF file. To do this, run the following command:

```
tesseract <pdf_file> <output_file> pdf
```

For example, to recognize text from a PDF file `example.pdf` and save the output in `example.txt`, run the following command:

```
tesseract example.pdf example.txt pdf
```

The output file `example.txt` will contain the recognized text from the PDF file.

## Helpful links

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Install Tesseract OCR on Ubuntu](https://www.how2shout.com/how-to/how-to-install-tesseract-ocr-on-ubuntu.html)

onelinerhub: [How can I use Tesseract OCR on Ubuntu 20.04?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-on-ubuntu------)