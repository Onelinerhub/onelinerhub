# How do I generate a QR code using PHP and TCPDF?
// plain

You can generate a QR code using PHP and TCPDF by following the steps below:

1. Download the TCPDF library from the [TCPDF website](https://tcpdf.org/).

2. Include the TCPDF library in your PHP script:

```php
require_once('tcpdf_include.php');
```

3. Create a new TCPDF document:

```php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```

4. Generate the QR code:

```php
$pdf->write2DBarcode('QR Code Text', 'QRCODE,H', 10, 10, 30, 30, $style, 'N');
```

5. Output the PDF document:

```php
$pdf->Output('qrcode.pdf', 'I');
```

The `write2DBarcode` function takes two parameters: the first is the text you want to encode in the QR code, and the second is the type of barcode you want to generate (in this case, `QRCODE,H` for a horizontal QR code). The other parameters are the X and Y coordinates of the upper-left corner of the QR code, the width and height of the QR code, an array of styling options, and whether the QR code should be printed as an image or as a vector.

For more information, you can check out the [TCPDF documentation](https://tcpdf.org/docs/code/classTCPDF#write2DBarcode) and the [TCPDF examples](https://tcpdf.org/examples/).

onelinerhub: [How do I generate a QR code using PHP and TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-generate-a-qr-code-using-php-and-tcpdf)