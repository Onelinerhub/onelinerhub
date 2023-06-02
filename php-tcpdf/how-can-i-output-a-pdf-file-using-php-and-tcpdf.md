# How can I output a PDF file using PHP and TCPDF?
// plain

Using the TCPDF library, you can output a PDF file using PHP. Here is an example code block to demonstrate this:
```
<?php

// Include the TCPDF library
require_once('tcpdf_include.php');

// Create a new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// Set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Author Name');
$pdf->SetTitle('PDF Document Title');

// Add a page
$pdf->AddPage();

// Set some content to print
$html = <<<EOD
<h1>PDF Document</h1>
<p>This is a sample PDF document.</p>
EOD;

// Print text using writeHTMLCell()
$pdf->writeHTMLCell(0, 0, '', '', $html, 0, 1, 0, true, '', true);

// Output the PDF document
$pdf->Output('example_001.pdf', 'I');

?>
```
This code will output a PDF file named `example_001.pdf`.

The code consists of the following parts:

1. `require_once('tcpdf_include.php');`: This will include the TCPDF library.
2. `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);`: This will create a new PDF document.
3. `$pdf->SetCreator(PDF_CREATOR); $pdf->SetAuthor('Author Name'); $pdf->SetTitle('PDF Document Title');`: This will set the document information.
4. `$pdf->AddPage();`: This will add a page to the PDF document.
5. `$html = <<<EOD ... EOD;`: This will set some content to print.
6. `$pdf->writeHTMLCell(0, 0, '', '', $html, 0, 1, 0, true, '', true);`: This will print the content using writeHTMLCell().
7. `$pdf->Output('example_001.pdf', 'I');`: This will output the PDF document.

## Helpful links

- [TCPDF Library](https://tcpdf.org/)
- [TCPDF Documentation](https://tcpdf.org/docs.php)

onelinerhub: [How can I output a PDF file using PHP and TCPDF?](https://onelinerhub.com/php-tcpdf/how-can-i-output-a-pdf-file-using-php-and-tcpdf)