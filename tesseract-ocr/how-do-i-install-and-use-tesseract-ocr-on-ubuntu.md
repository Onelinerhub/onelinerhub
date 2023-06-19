# How do I install and use Tesseract OCR on Ubuntu?
// plain

1. Install Tesseract OCR on Ubuntu:
  ```
  sudo apt-get install tesseract-ocr
  ```

2. Install additional language packs:
  ```
  sudo apt-get install tesseract-ocr-<lang>
  ```
  Replace `<lang>` with the two-letter code for the language you want to use. For example, to install the English language pack, use `sudo apt-get install tesseract-ocr-eng`.

3. Test Tesseract OCR:
  ```
  tesseract --version
  ```
  Output:
  ```
  tesseract 4.1.1
  leptonica-1.78.0
  libgif 5.1.4 : libjpeg 8d (libjpeg-turbo 1.5.2) : libpng 1.6.34 : libtiff 4.0.9 : zlib 1.2.11
  ```

4. Run Tesseract OCR on an image:
  ```
  tesseract image.png output
  ```
  This will create a text file `output.txt` with the OCR result.

5. Improve Tesseract OCR accuracy:
  You can improve the accuracy of Tesseract OCR by providing a training data file (`<lang>.traineddata`) for the language you are using. You can find these files on the [Tesseract OCR GitHub page](https://github.com/tesseract-ocr/tessdata).

6. Use Tesseract OCR from a programming language:
  Tesseract OCR can be used from a variety of programming languages, including Python, Java, and C++. You can find instructions for using Tesseract OCR from each of these languages on the [Tesseract OCR Wiki page](https://github.com/tesseract-ocr/tesseract/wiki).

7. Further reading:
  - [Tesseract OCR Wiki](https://github.com/tesseract-ocr/tesseract/wiki)
  - [Tesseract OCR GitHub page](https://github.com/tesseract-ocr/tessdata)
  - [Using Tesseract OCR with Python](https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/)

onelinerhub: [How do I install and use Tesseract OCR on Ubuntu?](https://onelinerhub.com/tesseract-ocr/how-do-i-install-and-use-tesseract-ocr-on-ubuntu)