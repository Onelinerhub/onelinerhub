# How can I replace TCPDF with PHP?
// plain

The easiest way to replace TCPDF with PHP is to use the FPDF library. FPDF is a free, open-source library for generating PDF documents with PHP. It supports all basic features of TCPDF, including page size and orientation, fonts, text, images, tables, headers, footers, and page numbers.

## Example code

```
<?php
require('fpdf.php');

$pdf = new FPDF();
$pdf->AddPage();
$pdf->SetFont('Arial','B',16);
$pdf->Cell(40,10,'Hello World!');
$pdf->Output();
```

## Output example

```
PDF file
```

The code above creates a PDF document with a single page containing the text "Hello World!".

The code consists of the following parts:

1. The `require('fpdf.php')` statement loads the FPDF library.
2. The `$pdf = new FPDF()` statement creates a new FPDF object.
3. The `$pdf->AddPage()` statement adds a new page to the document.
4. The `$pdf->SetFont('Arial','B',16)` statement sets the font to Arial, bold, and 16 points.
5. The `$pdf->Cell(40,10,'Hello World!')` statement adds the text "Hello World!" to the page.
6. The `$pdf->Output()` statement outputs the PDF document.

For more information, see the [FPDF website](http://www.fpdf.org/).

onelinerhub: [How can I replace TCPDF with PHP?](https://onelinerhub.com/php-tcpdf/how-can-i-replace-tcpdf-with-php)