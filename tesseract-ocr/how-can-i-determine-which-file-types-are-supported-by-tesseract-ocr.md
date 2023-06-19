# How can I determine which file types are supported by Tesseract OCR?
// plain

Tesseract OCR supports a wide range of file formats, including image files such as JPEG, TIFF, BMP, PNG, and PDF documents. To determine which file types are supported, you can use the `tesseract_cmd.get_supported_languages()` function. This function returns a list of supported file types.

For example, the following code will print out the supported file types:

```
from tesseract import tesseract_cmd

supported_file_types = tesseract_cmd.get_supported_languages()

print(supported_file_types)
```

## Output example

```
['JPEG', 'TIFF', 'BMP', 'PNG', 'PDF']
```

The code above uses the `tesseract_cmd.get_supported_languages()` function to get a list of supported file types. This list is then printed to the console.

## Helpful links

- [Tesseract Documentation](https://tesseract-ocr.github.io/tessdoc/Home.html)
- [Tesseract API Reference](https://tesseract-ocr.github.io/tessdoc/API-Reference.html)

onelinerhub: [How can I determine which file types are supported by Tesseract OCR?](https://onelinerhub.com/tesseract-ocr/how-can-i-determine-which-file-types-are-supported-by-tesseract-ocr)