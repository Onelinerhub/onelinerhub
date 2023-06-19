# How do I use Tesseract OCR to extract text from a ZIP file?
// plain

In order to use Tesseract OCR to extract text from a ZIP file, the following steps need to be taken:

1. Install Tesseract OCR on your computer. This can be done using the command `pip install tesseract-ocr`
2. Unzip the ZIP file using the command `unzip <file_name>.zip`
3. Extract the text from the file using the command `tesseract <file_name>.<file_extension> stdout`
4. The extracted text will be printed out in the terminal.

## Example code

```
unzip <file_name>.zip
tesseract <file_name>.<file_extension> stdout
```

## Output example

```
This is the extracted text from the file.
```

## Helpful links
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [How to Install Tesseract OCR on Ubuntu](https://www.howtoforge.com/tutorial/how-to-install-tesseract-on-ubuntu/)

onelinerhub: [How do I use Tesseract OCR to extract text from a ZIP file?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-to-extract-text-from-a-zip-file)