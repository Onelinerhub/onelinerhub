# How can I use OCR with PHP and Laravel?
// plain

OCR (Optical Character Recognition) is a technology that enables the recognition of text within images. It can be used with PHP and Laravel to extract text from images.

To use OCR with PHP and Laravel, you need to install a library such as [Tesseract](https://github.com/thiagoalessio/tesseract-ocr-for-php). After installation, you can use the library to extract text from images.

For example, the following code block can be used to extract text from an image:

```php
use thiagoalessio\TesseractOCR\TesseractOCR;

$image = 'image.png';
$text = (new TesseractOCR($image))->run();
echo $text;
```

The output of the code will be the extracted text from the image.

You can also use the [Intervention Image](http://image.intervention.io) library to manipulate the image before extracting the text. For example, the following code can be used to resize the image before extracting the text:

```php
use thiagoalessio\TesseractOCR\TesseractOCR;
use Intervention\Image\ImageManagerStatic as Image;

$image = 'image.png';
$image = Image::make($image)->resize(300, 200);
$text = (new TesseractOCR($image))->run();
echo $text;
```

The output of this code will be the extracted text from the resized image.

In conclusion, OCR can be used with PHP and Laravel to extract text from images. Libraries such as Tesseract and Intervention Image can be used to achieve this.

## Helpful links
- [Tesseract OCR for PHP](https://github.com/thiagoalessio/tesseract-ocr-for-php)
- [Intervention Image](http://image.intervention.io)

onelinerhub: [How can I use OCR with PHP and Laravel?](https://onelinerhub.com/php-laravel/how-can-i-use-ocr-with-php-and-laravel)