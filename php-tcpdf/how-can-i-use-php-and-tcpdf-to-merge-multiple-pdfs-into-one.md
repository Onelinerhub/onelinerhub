# How can I use PHP and TCPDF to merge multiple PDFs into one?
// plain

Using PHP and TCPDF, you can easily merge multiple PDFs into one. The following example code will combine two PDFs into a single PDF.

```
<?php
// Include the TCPDF library
require_once('tcpdf/tcpdf.php');

// Create a new TCPDF object
$pdf = new TCPDF();

// Open the first PDF
$pdf->setSourceFile('first.pdf');

// Import the first page of the first PDF
$tplIdx = $pdf->importPage(1);

// Add the first page of the first PDF
$pdf->addPage();
$pdf->useTemplate($tplIdx);

// Open the second PDF
$pdf->setSourceFile('second.pdf');

// Import the first page of the second PDF
$tplIdx = $pdf->importPage(1);

// Add the first page of the second PDF
$pdf->addPage();
$pdf->useTemplate($tplIdx);

// Output the merged PDF
$pdf->Output('merged.pdf', 'F');
```

This code will create a single PDF called `merged.pdf` containing the first page of `first.pdf` followed by the first page of `second.pdf`.

The code consists of the following parts:

1. Include the TCPDF library - `require_once('tcpdf/tcpdf.php');`
2. Create a new TCPDF object - `$pdf = new TCPDF();`
3. Open the first PDF - `$pdf->setSourceFile('first.pdf');`
4. Import the first page of the first PDF - `$tplIdx = $pdf->importPage(1);`
5. Add the first page of the first PDF - `$pdf->addPage(); $pdf->useTemplate($tplIdx);`
6. Open the second PDF - `$pdf->setSourceFile('second.pdf');`
7. Import the first page of the second PDF - `$tplIdx = $pdf->importPage(1);`
8. Add the first page of the second PDF - `$pdf->addPage(); $pdf->useTemplate($tplIdx);`
9. Output the merged PDF - `$pdf->Output('merged.pdf', 'F');`

For more information on how to use TCPDF to merge PDFs, please refer to the [TCPDF documentation](https://tcpdf.org/examples/example_047/).

onelinerhub: [How can I use PHP and TCPDF to merge multiple PDFs into one?](https://onelinerhub.com/php-tcpdf/how-can-i-use-php-and-tcpdf-to-merge-multiple-pdfs-into-one)