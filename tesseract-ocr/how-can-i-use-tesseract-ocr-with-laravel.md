# How can I use Tesseract OCR with Laravel?
// plain

Tesseract OCR (Optical Character Recognition) can be used with Laravel to recognize text from images. To do this, you will need to install Tesseract on your system and have the PHP Tesseract extension installed.

```
// Install Tesseract
sudo apt install tesseract-ocr

// Install PHP Tesseract extension
sudo apt install php-tesseract
```

The following code snippet demonstrates how to use Tesseract OCR with Laravel:

```
// Include Tesseract class
use thiagoalessio\TesseractOCR\TesseractOCR;

// Instantiate Tesseract
$tesseract = new TesseractOCR('/path/to/image.png');

// Recognize text from image
$text = $tesseract->run();

// Output result
echo $text;
```

The code above will read the image from the given path and output the recognized text.

## Code explanation

- `use thiagoalessio\TesseractOCR\TesseractOCR;` - This imports the TesseractOCR class from the `thiagoalessio/tesseract-ocr` package.
- `$tesseract = new TesseractOCR('/path/to/image.png');` - This instantiates Tesseract OCR with the given image path.
- `$text = $tesseract->run();` - This runs Tesseract OCR on the image and returns the recognized text.
- `echo $text;` - This outputs the recognized text.

For more information, please refer to the following links:
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [PHP Tesseract Extension](https://github.com/thiagoalessio/tesseract-ocr-for-php)
- [Laravel Tesseract](https://github.com/thiagoalessio/tesseract-ocr-for-php/tree/master/examples/laravel)

onelinerhub: [How can I use Tesseract OCR with Laravel?](https://onelinerhub.com/tesseract-ocr/how-can-i-use-tesseract-ocr-with-laravel)