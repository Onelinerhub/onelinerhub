# How do I install a language for Tesseract OCR?
// plain

1. First, download the language data files for the language you want to use for Tesseract OCR. The language data files are available from the [Tesseract OCR GitHub repository](https://github.com/tesseract-ocr/tessdata).

2. Extract the language data files and move them to the `tessdata` directory of the Tesseract OCR installation. For example, if you are using Linux, the Tesseract OCR installation directory is usually located at `/usr/share/tesseract-ocr/4.00/tessdata`.

3. To check if the language has been successfully installed, run the following command in the terminal:

```
tesseract --list-langs
```

## Output example

```
List of available languages (3):
eng
osd
spa
```

4. Now you can use the language you have installed to perform OCR on images. To do this, use the `-l` flag to specify the language you want to use:

```
tesseract image.png output -l eng
```

5. You can also use the `--print-parameters` flag to check the language you have installed and other parameters that Tesseract OCR is using:

```
tesseract --print-parameters
```

## Output example

```
Tesseract parameters:
  -l eng		Language: eng
  ...
```

6. If you want to use multiple languages, you can specify them with the `-l` flag, separated by `+`:

```
tesseract image.png output -l eng+spa
```

7. For more information about how to install and use languages for Tesseract OCR, see the [Tesseract OCR documentation](https://github.com/tesseract-ocr/tesseract/wiki).

onelinerhub: [How do I install a language for Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-do-i-install-a-language-for-tesseract-ocr)