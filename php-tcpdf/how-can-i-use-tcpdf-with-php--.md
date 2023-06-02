# How can I use TCPDF with PHP 8?
// plain

TCPDF is a PHP library used for creating PDF documents. It is compatible with PHP 8, and is easy to use. Here is an example of how to use it:

```
<?php

require_once('tcpdf/tcpdf.php');

// create new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Author Name');
$pdf->SetTitle('My Document');

// set default header data
$pdf->SetHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING, array(0,64,255), array(0,64,128));

// set header and footer fonts
$pdf->setHeaderFont(Array(PDF_FONT_NAME_MAIN, '', PDF_FONT_SIZE_MAIN));
$pdf->setFooterFont(Array(PDF_FONT_NAME_DATA, '', PDF_FONT_SIZE_DATA));

// set default monospaced font
$pdf->SetDefaultMonospacedFont(PDF_FONT_MONOSPACED);

// set margins
$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);
$pdf->SetHeaderMargin(PDF_MARGIN_HEADER);
$pdf->SetFooterMargin(PDF_MARGIN_FOOTER);

// set auto page breaks
$pdf->SetAutoPageBreak(TRUE, PDF_MARGIN_BOTTOM);

// set image scale factor
$pdf->setImageScale(PDF_IMAGE_SCALE_RATIO);

// set some language-dependent strings (optional)
if (@file_exists(dirname(__FILE__).'/lang/eng.php')) {
    require_once(dirname(__FILE__).'/lang/eng.php');
    $pdf->setLanguageArray($l);
}

// add a page
$pdf->AddPage();

// set font
$pdf->SetFont('helvetica', '', 10);

// output the HTML content
$pdf->writeHTML('<h1>Hello World!</h1>', true, false, true, false, '');

// reset pointer to the last page
$pdf->lastPage();

//Close and output PDF document
$pdf->Output('example.pdf', 'I');

```

This example will create a PDF document with the title "My Document" and the content "Hello World!".

The code consists of the following parts:

1. Require the TCPDF library: `require_once('tcpdf/tcpdf.php');`
2. Create a new PDF document: `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);`
3. Set document information: `$pdf->SetCreator(PDF_CREATOR);`, `$pdf->SetAuthor('Author Name');`, `$pdf->SetTitle('My Document');`
4. Set header data: `$pdf->SetHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING, array(0,64,255), array(0,64,128));`
5. Set header and footer fonts: `$pdf->setHeaderFont(Array(PDF_FONT_NAME_MAIN, '', PDF_FONT_SIZE_MAIN));`, `$pdf->setFooterFont(Array(PDF_FONT_NAME_DATA, '', PDF_FONT_SIZE_DATA));`
6. Set default monospaced font: `$pdf->SetDefaultMonospacedFont(PDF_FONT_MONOSPACED);`
7. Set margins: `$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);`, `$pdf->SetHeaderMargin(PDF_MARGIN_HEADER);`, `$pdf->SetFooterMargin(PDF_MARGIN_FOOTER);`
8. Set auto page breaks: `$pdf->SetAutoPageBreak(TRUE, PDF_MARGIN_BOTTOM);`
9. Set image scale factor: `$pdf->setImageScale(PDF_IMAGE_SCALE_RATIO);`
10. Set language-dependent strings (optional): `if (@file_exists(dirname(__FILE__).'/lang/eng.php')) { require_once(dirname(__FILE__).'/lang/eng.php'); $pdf->setLanguageArray($l); }`
11. Add a page: `$pdf->AddPage();`
12. Set font: `$pdf->SetFont('helvetica', '', 10);`
13. Output HTML content: `$pdf->writeHTML('<h1>Hello World!</h1>', true, false, true, false, '');`
14. Reset pointer to the last page: `$pdf->lastPage();`
15. Close and output PDF document: `$pdf->Output('example.pdf', 'I');`

For more information about using TCPDF with PHP 8, see the [TCPDF Documentation](https://tcpdf.org/docs/home/).

onelinerhub: [How can I use TCPDF with PHP 8?](https://onelinerhub.com/php-tcpdf/how-can-i-use-tcpdf-with-php--)