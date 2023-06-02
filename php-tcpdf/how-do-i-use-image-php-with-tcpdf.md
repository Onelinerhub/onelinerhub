# How do I use image.php with TCPDF?
// plain

In order to use image.php with TCPDF, you need to include the image.php file in your TCPDF project.

You can use the following code to add the image.php file:

```
require_once('image.php');
```

Once the image.php file is included, you can use the TCPDF image functions to add images to your PDF documents. For example, the following code will add an image to the PDF document:

```
$pdf->Image('image.jpg', 10, 10, 15, 15, 'JPG', '', '', true, 150, '', false, false, 1, false, false, false);
```

The code above will add the image.jpg file to the PDF document with the following parameters:

* 10 - The x-coordinate of the upper-left corner of the image
* 10 - The y-coordinate of the upper-left corner of the image
* 15 - The width of the image
* 15 - The height of the image
* 'JPG' - The type of the image
* '', '', true, 150 - Various other parameters

You can find more information about the TCPDF image functions in the [TCPDF Documentation](https://tcpdf.org/docs/source_docs/classTCPDF/#a7a0b7a8b8a0a1a8b3a7).

onelinerhub: [How do I use image.php with TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-use-image-php-with-tcpdf)