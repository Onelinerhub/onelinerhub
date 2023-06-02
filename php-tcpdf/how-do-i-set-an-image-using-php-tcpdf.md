# How do I set an image using PHP TCPDF?
// plain

Using the PHP library TCPDF, you can set an image using the `Image()` method. This method requires the following parameters:

1. `$file`: Path to the image file.
2. `$x`: Abscissa of the upper-left corner.
3. `$y`: Ordinate of the upper-left corner.
4. `$w`: Width of the image in the page.
5. `$h`: Height of the image in the page.
6. `$type`: Image format.
7. `$link`: URL or identifier returned by `AddLink()`.
8. `$align`: Indicates the alignment of the pointer next to image insertion relative to image height.

## Example code

```
$pdf->Image('example.jpg', 10, 10, 30, 40, 'JPG', '', 'T', false, 300, '', false, false, 1, false, false, false);
```

The output of the above code is a JPG image with a width of 30 and a height of 40, located at the coordinates (10, 10), with the text pointer aligned to the bottom of the image.

## Helpful links
- [TCPDF Image() Method](https://tcpdf.org/docs/source_docs/classTCPDF/#abd29f7b7e9f2e8c1a7f8f8e7f5f2f1f)
- [TCPDF Image() Method Parameters](https://tcpdf.org/docs/source_docs/classTCPDF/#a8f7c4b02b0b3d7c2f2b8d3d3f8f2d3e)

onelinerhub: [How do I set an image using PHP TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-set-an-image-using-php-tcpdf)