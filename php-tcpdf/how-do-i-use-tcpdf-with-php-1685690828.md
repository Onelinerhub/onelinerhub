# How do I use TCPDF with PHP?
// plain

1. TCPDF is a free open source PHP library used to generate PDF documents.

2. To use TCPDF with PHP, first download the library from [https://tcpdf.org/](https://tcpdf.org/).

3. Unzip the downloaded package and place the files in your project directory.

4. Create a PHP file and include the `tcpdf.php` file from the library.

```php
require_once('tcpdf/tcpdf.php');
```

5. Create an instance of the `TCPDF` class and set the page size, orientation, and margins.

```php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);
```

6. Add content to the PDF using the `AddPage()`, `SetFont()`, `Write()`, and other methods.

```php
$pdf->AddPage();
$pdf->SetFont('helvetica', '', 12);
$pdf->Write(0, 'Hello World!');
```

7. Output the PDF to the browser or save it to a file.

```php
$pdf->Output('example.pdf', 'I');
```

Links:
- [https://tcpdf.org/](https://tcpdf.org/)
- [https://tcpdf.org/docs/srcdoc/TCPDF/classTCPDF.html](https://tcpdf.org/docs/srcdoc/TCPDF/classTCPDF.html)

onelinerhub: [How do I use TCPDF with PHP?](https://onelinerhub.com/php-tcpdf/how-do-i-use-tcpdf-with-php-1685690828)