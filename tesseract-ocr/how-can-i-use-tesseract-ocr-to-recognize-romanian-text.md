# How can I use Tesseract OCR to recognize Romanian text?
// plain

Tesseract OCR can be used to recognize Romanian text by installing the Romanian language data files, configuring Tesseract to use the correct language, and then running Tesseract on an image or PDF file containing the Romanian text.

## Example code

```
# Install Romanian language data
sudo apt install tesseract-ocr-ron

# Configure Tesseract to use Romanian language
tesseract --list-langs
tesseract --lang ron

# Run Tesseract on an image or PDF file
tesseract image.png output
```

The output of the last command will be a text file containing the recognized Romanian text.

## Code explanation

- `sudo apt install tesseract-ocr-ron`: This command will install the Romanian language data files for Tesseract OCR.
- `tesseract --list-langs`: This command will list all languages available for Tesseract OCR.
- `tesseract --lang ron`: This command will configure Tesseract to use the Romanian language.
- `tesseract image.png output`: This command will run Tesseract OCR on an image file named `image.png` and save the recognized text to a file named `output`.

## Helpful links
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Installing Language Data Files](https://github.com/tesseract-ocr/tesseract/wiki/Data-Files#data-files-for-version-400-and-later)

onelinerhub: [How can I use Tesseract OCR to recognize Romanian text?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-to-recognize-romanian-text)