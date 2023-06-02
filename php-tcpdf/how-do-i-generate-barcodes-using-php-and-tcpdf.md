# How do I generate barcodes using PHP and TCPDF?
// plain

Generating barcodes using PHP and TCPDF is quite simple. The following example code uses TCPDF to generate a barcode in the Code 128 format:

```
<?php
// Include the TCPDF library
require_once('tcpdf_barcodes_1d.php');

// Create a new PDF document
$pdf = new TCPDF('P', 'mm', 'A4', true, 'UTF-8', false);

// Set document information
$pdf->SetCreator('TCPDF');
$pdf->SetAuthor('John Doe');
$pdf->SetTitle('Barcode Example');

// Set default monospaced font
$pdf->SetDefaultMonospacedFont(PDF_FONT_MONOSPACED);

// Set margins
$pdf->SetMargins(15, 15, 15);

// Set auto page breaks
$pdf->SetAutoPageBreak(TRUE, 15);

// Set font
$pdf->SetFont('helvetica', '', 10);

// Add a page
$pdf->AddPage();

// Print a barcode
$barcode = '1234567890';
$style = array(
    'position' => '',
    'align' => 'C',
    'stretch' => false,
    'fitwidth' => true,
    'cellfitalign' => '',
    'border' => true,
    'hpadding' => 'auto',
    'vpadding' => 'auto',
    'fgcolor' => array(0,0,0),
    'bgcolor' => false, //array(255,255,255),
    'text' => true,
    'font' => 'helvetica',
    'fontsize' => 8,
    'stretchtext' => 4
);

$pdf->write1DBarcode($barcode, 'C128', '', '', '', 18, 0.4, $style, 'N');

// Close and output PDF document
$pdf->Output('example_001.pdf', 'I');
?>
```

The example code above will generate a PDF document containing a Code 128 barcode with the value of `1234567890`. The code is composed of the following parts:

1. Include the TCPDF library: `require_once('tcpdf_barcodes_1d.php');`
2. Create a new PDF document: `$pdf = new TCPDF('P', 'mm', 'A4', true, 'UTF-8', false);`
3. Set document information: `$pdf->SetCreator('TCPDF');`, `$pdf->SetAuthor('John Doe');` and `$pdf->SetTitle('Barcode Example');`
4. Set default monospaced font: `$pdf->SetDefaultMonospacedFont(PDF_FONT_MONOSPACED);`
5. Set margins: `$pdf->SetMargins(15, 15, 15);`
6. Set auto page breaks: `$pdf->SetAutoPageBreak(TRUE, 15);`
7. Set font: `$pdf->SetFont('helvetica', '', 10);`
8. Add a page: `$pdf->AddPage();`
9. Print a barcode: `$pdf->write1DBarcode($barcode, 'C128', '', '', '', 18, 0.4, $style, 'N');`
10. Close and output PDF document: `$pdf->Output('example_001.pdf', 'I');`

For more information about generating barcodes using TCPDF, please refer to the [TCPDF documentation](https://tcpdf.org/docs/source_docs/classTCPDF/#abd9d6a8a2a7b4a5c5f3c9c2f9e3d9e1).

onelinerhub: [How do I generate barcodes using PHP and TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-generate-barcodes-using-php-and-tcpdf)