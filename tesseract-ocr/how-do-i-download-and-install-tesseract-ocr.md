# How do I download and install Tesseract OCR?
// plain

1. Download the latest version of Tesseract OCR from [GitHub](https://github.com/tesseract-ocr/tesseract/wiki/Downloads).
2. Extract the downloaded file.
3. Install the dependencies required for Tesseract OCR, such as Leptonica, which can be done using the following command: `sudo apt-get install libleptonica-dev`.
4. Compile the source code using the following command: `./autogen.sh && ./configure && make && make install`.
5. Add the Tesseract OCR installation directory to the system path. This can be done using the following command: `export PATH=$PATH:/usr/local/bin`.
6. Test the installation by running the following command: `tesseract --version`. The output should look like this:
```
tesseract 4.1.1
 leptonica-1.78.0
  libgif 5.1.4 : libjpeg 8d (libjpeg-turbo 1.5.2) : libpng 1.6.34 : libtiff 4.0.9 : zlib 1.2.11 : libwebp 0.6.1 : libopenjp2 2.3.0
```
7. You should now be able to use Tesseract OCR.

onelinerhub: [How do I download and install Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-download-and-install-tesseract-ocr)