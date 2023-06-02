# How do I use TCPDF in PHP to generate PDF documents?
// plain

TCPDF is a free and open source PHP library used to generate PDF documents from HTML and raw text. To use TCPDF, you need to include the TCPDF library in your PHP code.

```php
require_once('tcpdf/tcpdf.php');
```

You can then create an instance of the TCPDF class to generate the PDF document.

```php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```

## Code explanation

- `require_once()`: Includes the TCPDF library in your PHP code.
- `$pdf = new TCPDF()`: Instantiates a new TCPDF object.
- `$pdf->AddPage()`: Adds a new page to the PDF document.
- `$pdf->Write()`: Writes text or HTML content to the PDF document.
- `$pdf->Output()`: Outputs the PDF document to the browser or a file.

You can find the full documentation and examples of TCPDF at https://tcpdf.org/.

## Example


```php
require_once('tcpdf/tcpdf.php');

$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

$pdf->AddPage();

$html = '<h1>Hello World!</h1>';
$pdf->writeHTML($html, true, false, true, false, '');

$pdf->Output('example_001.pdf', 'I');
```

This will generate a PDF document with the text "Hello World!" and output it to the browser.

onelinerhub: [How do I use TCPDF in PHP to generate PDF documents?](https://onelinerhub.com/php-tcpdf/how-do-i-use-tcpdf-in-php-to-generate-pdf-documents)