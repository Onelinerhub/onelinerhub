# How do I install Tesseract OCR on Ubuntu?
// plain

1. Install the Tesseract OCR package using apt-get:
   ```
   sudo apt-get install tesseract-ocr
   ```
   This will install the Tesseract OCR package, as well as the language packages for English, Spanish, and other languages.

2. Install the Leptonica library:
   ```
   sudo apt-get install libleptonica-dev
   ```
   This library is required for Tesseract OCR to work properly.

3. Install the Tesseract OCR library:
   ```
   sudo apt-get install libtesseract-dev
   ```
   This library is the main Tesseract OCR library, and is necessary for Tesseract OCR to work.

4. Install the Tesseract OCR language data files:
   ```
   sudo apt-get install tesseract-ocr-eng
   ```
   This will install the language data files for English, which is necessary for Tesseract OCR to work properly.

5. Download and install the Tesseract OCR source code:
   ```
   wget https://github.com/tesseract-ocr/tesseract/archive/master.zip
   unzip master.zip
   cd tesseract-master
   ./autogen.sh
   ./configure
   make
   sudo make install
   ```
   This will download and install the Tesseract OCR source code, which is necessary for Tesseract OCR to work properly.

6. Verify that Tesseract OCR is installed correctly:
   ```
   tesseract -v
   ```
   This should output the version of Tesseract OCR that is installed.

7. Test Tesseract OCR by running it on an image:
   ```
   tesseract example.png output
   ```
   This will run Tesseract OCR on the example.png image, and output the results to the output file.

## Helpful links
- [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract/wiki)
- [Leptonica Library Documentation](http://www.leptonica.org/documentation.html)

onelinerhub: [How do I install Tesseract OCR on Ubuntu?](https://onelinerhub.com/tesseract-ocr/how-do-i-install-tesseract-ocr-on-ubuntu-1687146919)