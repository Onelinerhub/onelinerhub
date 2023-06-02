# How can I use TCPDF with PHP?
// plain

TCPDF is a PHP library that allows you to generate PDF documents from HTML code. It can be used with PHP to generate PDF documents with ease.

## Example code

```
<?php

// Include the TCPDF library
require_once('tcpdf/tcpdf.php');

// Create a new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// Set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetTitle('My PDF Document');

// Add a page
$pdf->AddPage();

// Set font
$pdf->SetFont('helvetica', '', 12);

// Output the HTML content
$pdf->writeHTML('<h1>Hello World!</h1>', true, false, true, false, '');

// Close and output the PDF document
$pdf->Output('my-document.pdf', 'I');
```

## Output example

PDF document named `my-document.pdf` is generated with "Hello World!" as the title.

## Code explanation

- `require_once('tcpdf/tcpdf.php');`: This line includes the TCPDF library.
- `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);`: This line creates a new PDF document with the specified parameters.
- `$pdf->SetCreator(PDF_CREATOR);`: This line sets the creator of the PDF document.
- `$pdf->SetTitle('My PDF Document');`: This line sets the title of the PDF document.
- `$pdf->AddPage();`: This line adds a page to the PDF document.
- `$pdf->SetFont('helvetica', '', 12);`: This line sets the font for the PDF document.
- `$pdf->writeHTML('<h1>Hello World!</h1>', true, false, true, false, '');`: This line writes HTML content to the PDF document.
- `$pdf->Output('my-document.pdf', 'I');`: This line outputs the PDF document.

## Helpful links
- [TCPDF Homepage](https://tcpdf.org/)
- [TCPDF Documentation](https://tcpdf.org/docs.php)
- [TCPDF Examples](https://tcpdf.org/examples/)

onelinerhub: [How can I use TCPDF with PHP?](https://onelinerhub.com/php-tcpdf/how-can-i-use-tcpdf-with-php-1685689343)