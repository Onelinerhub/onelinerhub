# How do I set the language for tesseract OCR?
// plain

The language for Tesseract OCR can be set using the `-l` command line argument. This argument takes an ISO 639-3 language code as its value. For example, to set the language to French:

```
tesseract -l fra image.jpg output
```

This will set the language to French and output the result to the `output` file.

## Code explanation


* `tesseract`: The name of the command line program.
* `-l`: The command line argument for setting the language.
* `fra`: The ISO 639-3 language code for French.
* `image.jpg`: The name of the image file to be processed.
* `output`: The name of the output file.

## Helpful links

* [Tesseract Command Line Usage](https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html)
* [ISO 639-3 Language Codes](https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes)

onelinerhub: [How do I set the language for tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-set-the-language-for-tesseract-ocr)