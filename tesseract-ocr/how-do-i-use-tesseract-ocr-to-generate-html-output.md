# How do I use tesseract OCR to generate HTML output?
// plain

Tesseract OCR is an open source Optical Character Recognition (OCR) engine developed by Google. It can be used to generate HTML output from scanned documents.

To use Tesseract OCR to generate HTML output, you need to install the Tesseract OCR engine and the Tesseract OCR command line tools.

Once the installation is complete, you can use the following command to generate HTML output from a scanned document:

```
tesseract <input-file> <output-file> --oem 1 -l eng --psm 3 hocr
```

The command above will generate an HTML output file containing the extracted text from the input file.

## Code explanation


* `tesseract` - This is the command for running Tesseract OCR.
* `<input-file>` - This is the path to the input file that needs to be processed.
* `<output-file>` - This is the path to the output file that will contain the extracted text.
* `--oem 1` - This is the option for selecting the Tesseract OCR engine.
* `-l eng` - This is the option for specifying the language of the input file.
* `--psm 3` - This is the option for specifying the page segmentation mode.
* `hocr` - This is the option for specifying the output format.

## Helpful links

* [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
* [Tesseract OCR Command Line Tools](https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage)

onelinerhub: [How do I use tesseract OCR to generate HTML output?](https://onelinerhub.com/tesseract-ocr/how-do-i-use-tesseract-ocr-to-generate-html-output)