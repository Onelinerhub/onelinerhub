# How do I install Tesseract-OCR using Yum?
// plain

Installing Tesseract-OCR using Yum is a simple process.

1. First, you need to install the EPEL repository. You can do this by running the following command in the terminal:
```
sudo yum install epel-release
```

2. Once the EPEL repository is installed, you can install Tesseract-OCR by running the following command:
```
sudo yum install tesseract
```

3. Once Tesseract-OCR is installed, you can verify the installation by running the following command:
```
tesseract --version
```
The output should look something like this:
```
tesseract 4.1.1
 leptonica-1.78.0
  libgif 5.1.4 : libjpeg 8d (libjpeg-turbo 1.5.2) : libpng 1.6.34 : libtiff 4.0.9 : zlib 1.2.11
```

4. You can also test the installation by running the following command:
```
tesseract <image_file> <output_file>
```
Where `<image_file>` is the path to the image file you want to OCR and `<output_file>` is the path where you want the output to be saved.

5. Once the OCR is complete, you can view the output file to see the text that was extracted from the image.

6. You can also use Tesseract-OCR from within your own applications. There are a number of different libraries and APIs available for different programming languages.

7. For more information on Tesseract-OCR, you can check out the official documentation at [https://github.com/tesseract-ocr/tesseract/wiki](https://github.com/tesseract-ocr/tesseract/wiki).

**## Helpful links**

- [https://github.com/tesseract-ocr/tesseract/wiki](https://github.com/tesseract-ocr/tesseract/wiki)
- [https://github.com/tesseract-ocr/tesseract/wiki/API](https://github.com/tesseract-ocr/tesseract/wiki/API)

onelinerhub: [How do I install Tesseract-OCR using Yum?](https://onelinerhub.com/tesseract-ocr/how-do-i-install-tesseract-ocr-using-yum)