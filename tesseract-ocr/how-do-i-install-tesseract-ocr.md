# How do I install Tesseract OCR?
// plain

1. Download the Tesseract OCR source code from the [GitHub page](https://github.com/tesseract-ocr/tesseract/wiki).
2. Install the required packages and dependencies for Tesseract OCR.
   ```
   sudo apt-get install autoconf automake libtool
   sudo apt-get install libpng-dev libjpeg62-dev libtiff-dev zlib1g-dev
   ```
3. Build and install Tesseract OCR:
   ```
   ./autogen.sh
   ./configure
   make
   sudo make install
   ```
4. Add the Tesseract OCR language data files. The language data files can be found in the [GitHub Tessdata Repository](https://github.com/tesseract-ocr/tessdata).
   ```
   wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata
   sudo mv eng.traineddata /usr/local/share/tessdata/
   ```
5. Test the Tesseract OCR installation.
   ```
   tesseract --version
   tesseract 4.1.1-rc1-25-g9707
   ```
6. To use Tesseract OCR, the command line syntax is as follows:
   ```
   tesseract <image> <output file> [-l <language>]
   ```
7. To get more information on using Tesseract OCR, please refer to the [Tesseract OCR Wiki page](https://github.com/tesseract-ocr/tesseract/wiki).

onelinerhub: [How do I install Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-install-tesseract-ocr)