# How do I use file_get_contents in PHP TCPDF?
// plain

Using `file_get_contents` in PHP TCPDF is a great way to add external content to a PDF document. The following example code shows how to use `file_get_contents` to add an HTML file to a PDF document:

```
<?php
// Include the TCPDF library
require_once('tcpdf_include.php');

// Create a new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// Get the contents of the HTML file
$html = file_get_contents('sample.html');

// Add a page to the document
$pdf->AddPage();

// Write the HTML to the document
$pdf->writeHTML($html, true, false, true, false, '');

// Output the document
$pdf->Output('sample.pdf', 'I');
```

## Code explanation


1. Include the TCPDF library - `require_once('tcpdf_include.php');`
2. Create a new PDF document - `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);`
3. Get the contents of the HTML file - `$html = file_get_contents('sample.html');`
4. Add a page to the document - `$pdf->AddPage();`
5. Write the HTML to the document - `$pdf->writeHTML($html, true, false, true, false, '');`
6. Output the document - `$pdf->Output('sample.pdf', 'I');`

This code will generate a PDF document with the contents of the `sample.html` file.

## Helpful links

- [TCPDF Documentation](https://tcpdf.org/docs/source_docs/classTCPDF/)
- [PHP file_get_contents() Function](https://www.w3schools.com/php/func_filesystem_file_get_contents.asp)

onelinerhub: [How do I use file_get_contents in PHP TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-use-file-get-contents-in-php-tcpdf)