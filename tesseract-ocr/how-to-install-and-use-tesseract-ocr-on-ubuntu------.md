# How to install and use Tesseract OCR on Ubuntu 22.04?
// plain

1. Install Tesseract OCR on Ubuntu 22.04 by running the following command in the terminal:
    ```
    sudo apt-get install tesseract-ocr
    ```

2. Use Tesseract OCR by running the following command in the terminal:
    ```
    tesseract <image-file-name> <output-file-name>
    ```
    For example:
    ```
    tesseract example.png output
    ```

3. To view the output, use the following command:
    ```
    cat output.txt
    ```

4. To improve the accuracy of the OCR results, you can use the following command to set the language:
    ```
    tesseract --list-langs
    ```
    This command will list the available languages. To set the language, use the following command:
    ```
    tesseract <image-file-name> <output-file-name> -l <language-code>
    ```
    For example:
    ```
    tesseract example.png output -l eng
    ```

5. To improve the accuracy of the OCR results further, you can use the following command to set the page segmentation mode:
    ```
    tesseract --psm <page-segmentation-mode>
    ```
    For example:
    ```
    tesseract example.png output -psm 6
    ```

6. To improve the accuracy of the OCR results even further, you can use the following command to set the OCR engine mode:
    ```
    tesseract --oem <OCR-engine-mode>
    ```
    For example:
    ```
    tesseract example.png output --oem 3
    ```

7. To learn more about Tesseract OCR, please refer to the [official documentation](https://github.com/tesseract-ocr/tesseract/wiki).

onelinerhub: [How to install and use Tesseract OCR on Ubuntu 22.04?](https://onelinerhub.com/tesseract-ocr/how-to-install-and-use-tesseract-ocr-on-ubuntu------)