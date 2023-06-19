# How to install Tesseract OCR on Windows?
// plain

Tesseract OCR is an open source tool for recognizing text from images. It can be installed on Windows using the following steps:

1. Install [Chocolatey](https://chocolatey.org/install) package manager for Windows.

2. Install Tesseract OCR using the command line:

```
choco install tesseract
```

3. Add Tesseract to the PATH environment variable.

4. Install the language packs for the languages you wish to use. For example, to install English language pack:

```
choco install tesseract-ocr-eng
```

5. Verify the installation by running the following command:

```
tesseract -v
```

## Output example

```
tesseract 4.1.1-rc2
 leptonica-1.78.0
  libgif 5.1.4 : libjpeg 8d (libjpeg-turbo 1.5.3) : libpng 1.6.35 : libtiff 4.0.9 : zlib 1.2.11
```

6. Test the installation by running the following command:

```
tesseract image.png output
```

7. Check the output file `output.txt` for the recognized text.

## Helpful links

- [Tesseract OCR on Windows](https://github.com/UB-Mannheim/tesseract/wiki#windows)
- [Chocolatey Installation Guide](https://chocolatey.org/install)

onelinerhub: [How to install Tesseract OCR on Windows?](https://onelinerhub.com/tesseract-ocr/how-to-install-tesseract-ocr-on-windows)