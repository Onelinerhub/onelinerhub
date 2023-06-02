# How can I add an image to a PDF document created using PHP TCPDF?
// plain

Adding an image to a PDF document created using PHP TCPDF is a straightforward process.

First, the image must be added to the PDF document using the `Image()` method. This method requires the file path of the image, the x and y coordinates of the image, the width and height of the image, and the image type as parameters.

For example:
```
$pdf->Image('images/image_file.jpg', 10, 10, 20, 20, 'JPG');
```

This code will add the image located at `images/image_file.jpg` to the PDF document at position (10, 10) with a width and height of 20.

## Code explanation


1. `Image()` method: Method used to add an image to the PDF document.
2. `images/image_file.jpg`: File path of the image.
3. `10` and `10`: x and y coordinates of the image.
4. `20` and `20`: width and height of the image.
5. `JPG`: Image type.

## Helpful links

1. [TCPDF Image() Method](https://tcpdf.org/docs/source_docs/classTCPDF/#a8f8a9e9c2d7c2c6f7d4dfa6f2f9f3b2)
2. [TCPDF Examples](https://tcpdf.org/examples/)

onelinerhub: [How can I add an image to a PDF document created using PHP TCPDF?](https://onelinerhub.com/php-tcpdf/how-can-i-add-an-image-to-a-pdf-document-created-using-php-tcpdf)