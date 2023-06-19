# How do I use the Tesseract OCR Linux command?
// plain

The Tesseract OCR Linux command is used to recognize text in images. To use it, first you need to install the Tesseract OCR package. On Ubuntu, this can be done by running the following command:

```
sudo apt-get install tesseract-ocr
```

Once the package is installed, you can use the Tesseract OCR command to recognize text in an image. For example, if you have an image named `example.jpg`, you can run the following command to recognize the text in the image and save it to a text file:

```
tesseract example.jpg output
```

This will create a file named `output.txt` containing the recognized text.

The Tesseract OCR command also supports many options for customizing the recognition process. For example, you can specify the language to use for recognition, the page segmentation mode, and the OCR engine mode. For a full list of options, you can run the following command:

```
tesseract --help
```

For more information on using the Tesseract OCR command, you can refer to the [Tesseract OCR documentation](https://github.com/tesseract-ocr/tesseract/wiki).

onelinerhub: [How do I use the Tesseract OCR Linux command?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-the-tesseract-ocr-linux-command)