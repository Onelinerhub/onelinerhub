# How can I use PHP and TCPDF to load a file?
// plain

Using PHP and TCPDF, you can easily load a file into a PDF document. The following example code will demonstrate how to do so:

```
<?php

// Include the TCPDF library
require_once('tcpdf_include.php');

// Create a new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// Set document information
$pdf->SetCreator('My Creator');
$pdf->SetAuthor('My Author');
$pdf->SetTitle('My Title');
$pdf->SetSubject('My Subject');

// Load a file
$pdf->AddPage();
$pdf->Image('myfile.jpg', 0, 0, 0, 0, '', '', '', false, 300, '', false, false, 0);

// Output the document
$pdf->Output('myfile.pdf', 'I');

?>
```

This code will create a new PDF document, set some document information, load the file `myfile.jpg` into the document, and output the document as `myfile.pdf`.

The code consists of the following parts:

1. `require_once('tcpdf_include.php');` - This line includes the TCPDF library.
2. `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);` - This line creates a new PDF document.
3. `$pdf->SetCreator('My Creator');` - This line sets the document creator.
4. `$pdf->SetAuthor('My Author');` - This line sets the document author.
5. `$pdf->SetTitle('My Title');` - This line sets the document title.
6. `$pdf->SetSubject('My Subject');` - This line sets the document subject.
7. `$pdf->AddPage();` - This line adds a page to the document.
8. `$pdf->Image('myfile.jpg', 0, 0, 0, 0, '', '', '', false, 300, '', false, false, 0);` - This line loads the file `myfile.jpg` into the document.
9. `$pdf->Output('myfile.pdf', 'I');` - This line outputs the document as `myfile.pdf`.

For more information about using TCPDF, please see the [TCPDF documentation](https://tcpdf.org/docs/).

onelinerhub: [How can I use PHP and TCPDF to load a file?](https://onelinerhub.com/php-tcpdf/how-can-i-use-php-and-tcpdf-to-load-a-file)