# How do I use tesseract OCR from the command line?
// plain

Tesseract OCR is an open source Optical Character Recognition (OCR) engine that can be used to recognize text from images. It can be used from the command line by using the `tesseract` command.

The basic syntax for using `tesseract` is as follows:

```
tesseract <input_file> <output_file>
```

Where `<input_file>` is the path to the image file containing the text to be recognized and `<output_file>` is the path to the output file where the recognized text will be written.

For example, to recognize text from an image file named `example.png` and write the recognized text to a file named `example.txt`, the command would be:

```
tesseract example.png example.txt
```

The command will output a message like:

```
Tesseract Open Source OCR Engine v4.1.1 with Leptonica
```

indicating that the command was successful. The recognized text can then be found in the `example.txt` file.

In addition to the basic syntax, Tesseract also supports a number of options for controlling how the text is recognized. For example, you can specify the language of the text to be recognized, the page segmentation mode, and the OCR engine mode. For more information about these options, see the [Tesseract documentation](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html).

## Code explanation
**

- `tesseract`: command to run Tesseract OCR
- `<input_file>`: path to the image file containing the text to be recognized
- `<output_file>`: path to the output file where the recognized text will be written

**## Helpful links**

- [Tesseract documentation](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html)

onelinerhub: [How do I use tesseract OCR from the command line?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-from-the-command-line)