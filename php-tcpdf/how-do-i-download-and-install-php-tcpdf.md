# How do I download and install PHP TCPDF?
// plain

1. Download the latest version of [TCPDF](https://tcpdf.org/download) library.
2. Extract the downloaded file in a directory of your choice.
3. Include the TCPDF library in your PHP script using `require_once`:
```php
require_once('/path/to/tcpdf/tcpdf.php');
```
4. Create a new TCPDF object:
```php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```
5. Configure the TCPDF object according to your needs.
6. Generate the PDF using `$pdf->Output()`:
```php
$pdf->Output('example.pdf', 'I');
```
7. The PDF file will be generated and sent to the browser.

onelinerhub: [How do I download and install PHP TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-download-and-install-php-tcpdf)