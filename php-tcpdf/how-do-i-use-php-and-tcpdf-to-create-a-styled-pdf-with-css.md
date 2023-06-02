# How do I use PHP and TCPDF to create a styled PDF with CSS?
// plain

Using PHP and TCPDF, it is possible to create a styled PDF with CSS. To do this, first you will need to include the TCPDF library in your PHP script. Then, you will need to set the page size, margins, and orientation. After that, you can use HTML and CSS to style the PDF.

## Example code

```
<?php

require_once('tcpdf.php');

// create new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Author Name');
$pdf->SetTitle('Title of PDF');
$pdf->SetSubject('Subject of PDF');
$pdf->SetKeywords('keyword1, keyword2');

// set default header data
$pdf->SetHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING, array(0,64,255), array(0,64,128));
$pdf->setFooterData(array(0,64,0), array(0,64,128));

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

// add a page
$pdf->AddPage();

// set font
$pdf->SetFont('helvetica', 'B', 20);

// add a page
$pdf->Write(0, 'Styled PDF with CSS', '', 0, 'C', true, 0, false, false, 0);

// set style for barcode
$style = array(
    'border' => 2,
    'vpadding' => 'auto',
    'hpadding' => 'auto',
    'fgcolor' => array(0,0,0),
    'bgcolor' => false, //array(255,255,255)
    'module_width' => 1, // width of a single module in points
    'module_height' => 1 // height of a single module in points
);

// QRCODE,L : QR-CODE Low error correction
$pdf->write2DBarcode('www.tcpdf.org', 'QRCODE,L', 20, 30, 50, 50, $style, 'N');

//Close and output PDF document
$pdf->Output('example_001.pdf', 'I');

```

The example code above will create a PDF with the text "Styled PDF with CSS" and a QR code.

## Code explanation

1. Include the TCPDF library - `require_once('tcpdf.php');`
2. Set the page size, margins, and orientation - `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);`
3. Set document information - `$pdf->SetCreator(PDF_CREATOR);`
4. Set default header data - `$pdf->SetHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING, array(0,64,255), array(0,64,128));`
5. Set header and footer fonts - `$pdf->setHeaderFont(Array(PDF_FONT_NAME_MAIN, '', PDF_FONT_SIZE_MAIN));`
6. Set default monospaced font - `$pdf->SetDefaultMonospacedFont(PDF_FONT_MONOSPACED);`
7. Set margins - `$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);`
8. Set auto page breaks - `$pdf->SetAutoPageBreak(TRUE, PDF_MARGIN_BOTTOM);`
9. Set image scale factor - `$pdf->setImageScale(PDF_IMAGE_SCALE_RATIO);`
10. Add a page - `$pdf->AddPage();`
11. Set font - `$pdf->SetFont('helvetica', 'B', 20);`
12. Write text - `$pdf->Write(0, 'Styled PDF with CSS', '', 0, 'C', true, 0, false, false, 0);`
13. Set style for barcode - `$style = array(...);`
14. Write barcode - `$pdf->write2DBarcode('www.tcpdf.org', 'QRCODE,L', 20, 30, 50, 50, $style, 'N');`
15. Output PDF - `$pdf->Output('example_001.pdf', 'I');`

## Helpful links
- [TCPDF Documentation](https://tcpdf.org/docs/code-examples/basic/)
- [Creating a PDF with TCPDF in PHP](https://www.sitepoint.com/creating-pdf-php-tcpdf/)

onelinerhub: [How do I use PHP and TCPDF to create a styled PDF with CSS?](https://onelinerhub.com/php-tcpdf/how-do-i-use-php-and-tcpdf-to-create-a-styled-pdf-with-css)