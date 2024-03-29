# How can I use Tesseract OCR in a PHP project?
// plain

Tesseract OCR can be used in a PHP project by using the [Tesseract-OCR-for-PHP](https://github.com/thiagoalessio/tesseract-ocr-for-php) package. This package provides a wrapper for the Tesseract OCR command line tool.

## Example code


```
<?php

require 'vendor/autoload.php';

use thiagoalessio\TesseractOCR\TesseractOCR;

echo (new TesseractOCR('image.png'))->run();

```

## Output example


```
Hello World
```

The code above will run the Tesseract OCR command line tool on the image `image.png` and output the recognized text.

The code consists of three parts:

1. `require 'vendor/autoload.php';`: This is used to include the autoloader generated by Composer, which is used to autoload the classes from the `thiagoalessio\TesseractOCR` namespace.

2. `use thiagoalessio\TesseractOCR\TesseractOCR;`: This is used to import the `TesseractOCR` class from the `thiagoalessio\TesseractOCR` namespace.

3. `echo (new TesseractOCR('image.png'))->run();`: This is used to create an instance of the `TesseractOCR` class with the given image path and run the OCR process. The recognized text is then outputted.

## Helpful links

- [Tesseract-OCR-for-PHP](https://github.com/thiagoalessio/tesseract-ocr-for-php)
- [Tesseract OCR](https://github.com/tesseract-ocr/)

onelinerhub: [How can I use Tesseract OCR in a PHP project?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-in-a-php-project)