# How can I use TCPDF in PHP?
// plain

TCPDF is a PHP library used to generate PDF documents. It can be used to create PDF files dynamically, which can be used for invoices, contracts, and other documents.

To use TCPDF in PHP, you first need to include the library in your project:

```php
require_once('/path/to/tcpdf.php');
```

Then, you need to create an instance of the TCPDF class:

```php
$pdf = new TCPDF();
```

You can then add content to the PDF using the `writeHTML()` method:

```php
$html = '<h1>My PDF</h1>';
$pdf->writeHTML($html);
```

Finally, you can output the PDF to the browser or save it to a file using the `Output()` method:

```php
$pdf->Output('my_pdf.pdf', 'D');
```

The `Output()` method takes two parameters:

1. The name of the output file.
2. The output destination. `D` is for download, `I` is for inline, and `F` is for saving to a file.

For more information on using TCPDF, you can check out the [official documentation](https://tcpdf.org/docs/).

onelinerhub: [How can I use TCPDF in PHP?](https://onelinerhub.com/php-tcpdf/how-can-i-use-tcpdf-in-php)