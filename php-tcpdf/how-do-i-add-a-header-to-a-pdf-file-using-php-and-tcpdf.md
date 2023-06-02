# How do I add a header to a PDF file using PHP and TCPDF?
// plain

Using the [TCPDF library](https://tcpdf.org/), you can add a header to a PDF file using PHP. Here is an example code block to get you started:

```php
<?php
// Include the TCPDF library
require_once('tcpdf_include.php');

// create new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('My Name');
$pdf->SetTitle('My PDF Title');
$pdf->SetSubject('My PDF Subject');
$pdf->SetKeywords('My, PDF, Keywords');

// set header and footer
$pdf->setHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING);

// set margins
$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);
$pdf->SetHeaderMargin(PDF_MARGIN_HEADER);
$pdf->SetFooterMargin(PDF_MARGIN_FOOTER);

// set auto page breaks
$pdf->SetAutoPageBreak(TRUE, PDF_MARGIN_BOTTOM);

// set image scale factor
$pdf->setImageScale(PDF_IMAGE_SCALE_RATIO);

// Add a page
$pdf->AddPage();

// Print a text
$pdf->Write(0, 'My PDF header', '', 0, 'C', true, 0, false, false, 0);

// Close and output PDF document
$pdf->Output('example_001.pdf', 'I');
```

This code will generate a PDF file with a header.

The code is composed of the following parts:

1. Include the TCPDF library: `require_once('tcpdf_include.php');`
2. Create a new PDF document: `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);`
3. Set document information: `$pdf->SetCreator(PDF_CREATOR);`
4. Set header and footer: `$pdf->setHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING);`
5. Set margins: `$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);`
6. Set auto page breaks: `$pdf->SetAutoPageBreak(TRUE, PDF_MARGIN_BOTTOM);`
7. Set image scale factor: `$pdf->setImageScale(PDF_IMAGE_SCALE_RATIO);`
8. Add a page: `$pdf->AddPage();`
9. Print a text: `$pdf->Write(0, 'My PDF header', '', 0, 'C', true, 0, false, false, 0);`
10. Close and output PDF document: `$pdf->Output('example_001.pdf', 'I');`

## Helpful links

* [TCPDF Library](https://tcpdf.org/)
* [TCPDF Documentation](https://tcpdf.org/docs.php)

onelinerhub: [How do I add a header to a PDF file using PHP and TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-add-a-header-to-a-pdf-file-using-php-and-tcpdf)