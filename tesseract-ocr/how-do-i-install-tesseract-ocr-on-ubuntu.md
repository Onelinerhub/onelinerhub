# How do I install Tesseract OCR on Ubuntu?
// plain

1. Install Tesseract OCR on Ubuntu by using the following command:

```sudo apt-get install tesseract-ocr```

2. After the installation is complete, you can check the version of Tesseract OCR installed by using the following command:

```tesseract --version```

## Output example
 tesseract 4.1.0-rc2

3. You can also use the Tesseract OCR command line tool to recognize text from images by using the following command:

```tesseract image.png output```

4. To install the Tesseract OCR language data, use the following command:

```sudo apt-get install tesseract-ocr-[language]```

Replace [language] with the language data you want to install.

5. To use the language data, use the following command:

```tesseract image.png output -l [language]```

Replace [language] with the language data you want to use.

6. If you want to install additional language data, you can download the language data from the [Tesseract OCR GitHub repository](https://github.com/tesseract-ocr/tessdata).

7. After downloading the language data, copy it to the `/usr/share/tesseract-ocr/4.00/tessdata` folder.

## Helpful links

- [Tesseract OCR GitHub repository](https://github.com/tesseract-ocr/tessdata)
- [Tesseract OCR documentation](https://github.com/tesseract-ocr/tesseract/wiki)

onelinerhub: [How do I install Tesseract OCR on Ubuntu?](https://onelinerhub.com/tesseract-ocr/how-do-i-install-tesseract-ocr-on-ubuntu)