# How do I download the Tesseract OCR engine?
// plain

1. Tesseract OCR engine can be downloaded from its official page hosted on [GitHub](https://github.com/tesseract-ocr/tesseract/wiki).
2. You can also download Tesseract from its [releases page](https://github.com/tesseract-ocr/tesseract/releases).
3. To download Tesseract, you can use the command line. For example, to download version 4.1.0, you can use the command `wget https://github.com/tesseract-ocr/tesseract/archive/4.1.0.tar.gz`:
    ```
    wget https://github.com/tesseract-ocr/tesseract/archive/4.1.0.tar.gz
    ```
4. After downloading the file, you can extract it using the command `tar -xvf 4.1.0.tar.gz`:
    ```
    tar -xvf 4.1.0.tar.gz
    ```
5. After extracting the file, you can install Tesseract by running the `make` command in the extracted directory:
    ```
    make
    ```
6. Once the installation is complete, you can test the installation by running the `tesseract --version` command:
    ```
    tesseract --version
    ```
    Output:
    ```
    tesseract 4.1.0
    leptonica-1.78.0
    libgif 5.1.4 : libjpeg 8d (libjpeg-turbo 1.5.2) : libpng 1.6.34 : libtiff 4.0.9 : zlib 1.2.11 : libwebp 0.6.1 : libopenjp2 2.3.0
7. For more detailed instructions, you can refer to the [official installation guide](https://github.com/tesseract-ocr/tesseract/wiki/Compiling).

onelinerhub: [How do I download the Tesseract OCR engine?](https://onelinerhub.com/tesseract-ocr/how-do-i-download-the-tesseract-ocr-engine)