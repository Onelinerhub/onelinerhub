# How do I use PHP and TCPDF to convert HTML to PDF?
// plain

Using PHP and TCPDF to convert HTML to PDF is relatively straightforward. To get started, you'll need to include the TCPDF library in your project.

```php
require_once('tcpdf_include.php');
```

Next, you'll need to create a new instance of the TCPDF class and set the page size, margins, and font.

```php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);
$pdf->SetHeaderMargin(PDF_MARGIN_HEADER);
$pdf->SetFooterMargin(PDF_MARGIN_FOOTER);
$pdf->SetAutoPageBreak(TRUE, PDF_MARGIN_BOTTOM);
$pdf->SetFont('helvetica', '', 10);
```

Once the PDF instance is set up, you can use the `writeHTML` method to convert your HTML into a PDF.

```php
$html = '<h1>My HTML</h1><p>Some sample text.</p>';
$pdf->writeHTML($html, true, false, true, false, '');
```

Finally, you can output the PDF to the browser or save it to a file.

```php
$pdf->Output('my-pdf.pdf', 'I');
```

## Code explanation


1. `require_once('tcpdf_include.php');`: Includes the TCPDF library in your project.
2. `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);`: Creates a new instance of the TCPDF class.
3. `$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);`: Sets the page margins.
4. `$pdf->SetHeaderMargin(PDF_MARGIN_HEADER);`: Sets the header margin.
5. `$pdf->SetFooterMargin(PDF_MARGIN_FOOTER);`: Sets the footer margin.
6. `$pdf->SetAutoPageBreak(TRUE, PDF_MARGIN_BOTTOM);`: Sets the page break.
7. `$pdf->SetFont('helvetica', '', 10);`: Sets the font.
8. `$html = '<h1>My HTML</h1><p>Some sample text.</p>';`: Creates a sample HTML string.
9. `$pdf->writeHTML($html, true, false, true, false, '');`: Converts the HTML into a PDF.
10. `$pdf->Output('my-pdf.pdf', 'I');`: Outputs the PDF to the browser or saves it to a file.

## Helpful links

- [TCPDF Documentation](https://tcpdf.org/docs.php)
- [TCPDF GitHub Repository](https://github.com/tecnickcom/TCPDF)

onelinerhub: [How do I use PHP and TCPDF to convert HTML to PDF?](https://onelinerhub.com/php-tcpdf/how-do-i-use-php-and-tcpdf-to-convert-html-to-pdf)