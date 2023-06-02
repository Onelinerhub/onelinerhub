# How can I use TCPDF's writeHTML() function in PHP?
// plain

The `writeHTML()` function in TCPDF is used to render HTML code into a PDF document. It takes two parameters: the HTML code and a boolean indicating whether to use the default font or not. Here is an example of how to use it:

```php
<?php
// Include the TCPDF library
require_once('tcpdf/tcpdf.php');

// Create a new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// Set document information
$pdf->SetCreator('My App');
$pdf->SetAuthor('Me');
$pdf->SetTitle('My PDF Document');

// Add a page
$pdf->AddPage();

// Render HTML code
$html = '<h1>Hello World!</h1>';
$pdf->writeHTML($html, true);

// Output the PDF
$pdf->Output('my_document.pdf', 'I');

```

This code will generate a PDF document with a single page containing the text `Hello World!`.

## Code explanation


1. `require_once('tcpdf/tcpdf.php');`: This includes the TCPDF library in the script.
2. `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);`: This creates a new PDF document.
3. `$pdf->SetCreator('My App');`: This sets the document creator.
4. `$pdf->SetAuthor('Me');`: This sets the document author.
5. `$pdf->SetTitle('My PDF Document');`: This sets the document title.
6. `$pdf->AddPage();`: This adds a page to the document.
7. `$html = '<h1>Hello World!</h1>';`: This creates a string containing the HTML code to be rendered.
8. `$pdf->writeHTML($html, true);`: This renders the HTML code into the PDF document.
9. `$pdf->Output('my_document.pdf', 'I');`: This outputs the PDF document.

For more information, see the [TCPDF Documentation](https://tcpdf.org/docs/).

onelinerhub: [How can I use TCPDF's writeHTML() function in PHP?](https://onelinerhub.com/php-tcpdf/how-can-i-use-tcpdf-s-writehtml---function-in-php)