# How do I install Tesseract OCR?
// plain

1. Tesseract OCR can be installed on Windows, Mac, and Linux operating systems.
2. On Windows, you can install Tesseract OCR by downloading the executable from [this link](https://github.com/UB-Mannheim/tesseract/wiki).
3. On Mac, you can install Tesseract OCR with [Homebrew](https://brew.sh/) by running the following command in the terminal:
```
brew install tesseract
```
4. On Linux, you can install Tesseract OCR by running the following command in the terminal:
```
sudo apt-get install tesseract-ocr
```
5. After installation, you can verify the installation by running the following command in the terminal:
```
tesseract --version
```
The output should be something like:
```
tesseract 4.1.1
 leptonica-1.78.0
  libgif 5.1.4 : libjpeg 8d (libjpeg-turbo 1.5.2) : libpng 1.6.34 : libtiff 4.0.9 : zlib 1.2.11
```
6. Once Tesseract OCR is installed, you can use it to recognize text in images by running the following command in the terminal:
```
tesseract image.png output
```
7. This will create a file called `output.txt` in the same directory as the image, which contains the recognized text.

For more information on how to use Tesseract OCR, please refer to the [official documentation](https://tesseract-ocr.github.io/tessdoc/Home.html).

onelinerhub: [How do I install Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-install-tesseract-ocr-1687138994)