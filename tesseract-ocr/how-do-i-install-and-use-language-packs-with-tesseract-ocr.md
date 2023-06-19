# How do I install and use language packs with Tesseract OCR?
// plain

1. Download the language pack of your choice from the [Tesseract OCR language packs](https://github.com/tesseract-ocr/tessdata) repository.
2. Extract the language pack files to the `tessdata` directory. On Linux, this is usually `/usr/share/tesseract-ocr/4.00/tessdata/`
3. Use the `-l` parameter in the Tesseract command line to specify the language you want to use. For example, `tesseract input.jpg output -l deu`
4. To verify that the language pack has been loaded, you can use the `--list-langs` command. This will output a list of all the languages available to Tesseract.

## Example code


```
tesseract input.jpg output -l deu
tesseract --list-langs
```

Example output:

```
List of available languages (2):
deu
eng
```

## Helpful links
- [Tesseract OCR language packs](https://github.com/tesseract-ocr/tessdata)

onelinerhub: [How do I install and use language packs with Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-install-and-use-language-packs-with-tesseract-ocr)