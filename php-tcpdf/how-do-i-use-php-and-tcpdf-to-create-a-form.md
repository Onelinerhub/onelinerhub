# How do I use PHP and TCPDF to create a form?
// plain

Using PHP and TCPDF you can create a form by following these steps:

1. Include the TCPDF library in your PHP code by using `require_once('tcpdf.php');`
2. Create an instance of the TCPDF class with `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);`
3. Set the document information with `$pdf->SetCreator(PDF_CREATOR);` and other `$pdf->Set*` functions
4. Add a page with `$pdf->AddPage();`
5. Set the font with `$pdf->SetFont('helvetica', '', 10);`
6. Add the form elements with `$pdf->Cell(40, 10, 'Name:', 1, 0, 'L');` and other `$pdf->Cell` functions
7. Output the PDF with `$pdf->Output('example_form.pdf', 'I');`

## Example code

```
<?php
require_once('tcpdf.php');

// create new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('John Doe');
$pdf->SetTitle('Example Form');
$pdf->SetSubject('Example Form');
$pdf->SetKeywords('TCPDF, PDF, example, test, guide');

// add a page
$pdf->AddPage();

// set font
$pdf->SetFont('helvetica', '', 10);

// add form elements
$pdf->Cell(40, 10, 'Name:', 1, 0, 'L');
$pdf->Cell(40, 10, '', 1, 0, 'L');
$pdf->Cell(40, 10, 'Email:', 1, 0, 'L');
$pdf->Cell(40, 10, '', 1, 1, 'L');

// output the PDF
$pdf->Output('example_form.pdf', 'I');
```

## Output example
 A PDF file containing a form with two empty fields (Name and Email) and their respective labels.

onelinerhub: [How do I use PHP and TCPDF to create a form?](https://onelinerhub.com/php-tcpdf/how-do-i-use-php-and-tcpdf-to-create-a-form)