# How can I install and use tesseract OCR on a Linux system?
// plain

1. Install tesseract OCR on a Linux system by running the following command in the terminal: `sudo apt-get install tesseract-ocr`
2. Once installed, you can use tesseract OCR by running the following command in the terminal: `tesseract <image-file-path> <output-file-path>`
3. For example, if you want to convert an image file called `example.png` to a text file called `example.txt`, you can run the following command: `tesseract example.png example.txt`
4. This will generate a text file called `example.txt` containing the text extracted from the image file `example.png`
5. You can also specify the language of the text you want to extract by adding the `-l` flag followed by the language code, for example to extract text from `example.png` in French you would run the following command: `tesseract -l fra example.png example.txt`
6. You can also set the page segmentation mode by adding the `-psm` flag followed by the page segmentation mode number, for example to extract text from `example.png` in French using the single column page segmentation mode you would run the following command: `tesseract -l fra -psm 6 example.png example.txt`
7. For more information on how to use tesseract OCR on a Linux system, please refer to the [tesseract OCR documentation](https://github.com/tesseract-ocr/tesseract/wiki).

onelinerhub: [How can I install and use tesseract OCR on a Linux system?](https://onelinerhub.com/tesseract-ocr/how-can-i-install-and-use-tesseract-ocr-on-a-linux-system)