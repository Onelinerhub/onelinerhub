# How do I use Tesseract OCR with the command line?
// plain

Tesseract OCR is an open-source command-line tool used for recognizing text from images. To use Tesseract OCR with the command line, perform the following steps:

1. Install Tesseract OCR on your system.
2. Download the image file that you want to recognize text from.
3. Open a command line or terminal window.
4. Navigate to the directory containing the image file.
5. Run the following command, replacing `input.jpg` with the name of your image file:

```
tesseract input.jpg output
```

This command will create a file called `output.txt` in the same directory, which will contain the recognized text.

6. To view the recognized text, open the `output.txt` file in a text editor.
7. (Optional) To save the recognized text to a different file, run the following command, replacing `output.txt` with the desired path and filename:

```
tesseract input.jpg output --oem 0 -psm 6 txt output.txt
```

This command will save the recognized text to `output.txt`.

## Helpful links

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Command Line Usage](https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage)

onelinerhub: [How do I use Tesseract OCR with the command line?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-with-the-command-line)