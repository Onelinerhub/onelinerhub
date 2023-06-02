# How can I generate a QR code using PHP and TCPDF?
// plain

Using PHP and TCPDF, you can generate a QR code by following these steps:

1. Include the TCPDF library in your PHP file:
```php
require_once('tcpdf/tcpdf.php');
```

2. Create a new instance of the TCPDF class:
```php
$pdf = new TCPDF();
```

3. Generate the QR code using the `QRcode` method:
```php
$pdf->write2DBarcode('This is a QR code', 'QRCODE,H', 10, 10, 20, 20, $style, 'N');
```

4. Output the PDF file using the `Output` method:
```php
$pdf->Output('example.pdf', 'I');
```

The parts of the code are as follows:

* `require_once('tcpdf/tcpdf.php');`: This includes the TCPDF library in the PHP file.

* `$pdf = new TCPDF();`: This creates a new instance of the TCPDF class.

* `$pdf->write2DBarcode('This is a QR code', 'QRCODE,H', 10, 10, 20, 20, $style, 'N');`: This generates the QR code using the `QRcode` method, where 'This is a QR code' is the text to be encoded, 'QRCODE,H' is the type of barcode, 10, 10 is the x and y position of the barcode, 20, 20 is the width and height of the barcode, and 'N' is the mode of the barcode.

* `$pdf->Output('example.pdf', 'I');`: This outputs the PDF file using the `Output` method, where 'example.pdf' is the name of the file and 'I' is the output mode (I for inline, D for download).

## Helpful links

* [TCPDF Library Documentation](https://tcpdf.org/docs/home/)
* [QR Code Generator with PHP](https://www.codexworld.com/generate-qr-code-using-php/)

onelinerhub: [How can I generate a QR code using PHP and TCPDF?](https://onelinerhub.com/php-tcpdf/how-can-i-generate-a-qr-code-using-php-and-tcpdf)