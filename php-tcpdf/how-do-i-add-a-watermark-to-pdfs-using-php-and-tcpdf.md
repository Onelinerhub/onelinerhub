# How do I add a watermark to PDFs using PHP and TCPDF?
// plain

Using PHP and TCPDF, you can add a watermark to PDFs in the following way:

1. Create a new PDF document using the `TCPDF()` constructor.
2. Use the `SetAlpha()` method to set the transparency of the watermark image.
3. Use the `Image()` method to add the watermark image to the PDF document.
4. Use the `SetXY()` method to set the coordinates of the watermark image.
5. Use the `SetFont()` method to set the font size and type of the watermark text.
6. Use the `SetTextColor()` method to set the color of the watermark text.
7. Use the `Cell()` method to add the watermark text to the PDF document.

## Example code

```
<?php

// Include the TCPDF library
require_once('tcpdf.php');

// Create a new PDF document
$pdf = new TCPDF();

// Set the transparency of the watermark image
$pdf->SetAlpha(0.2);

// Add the watermark image to the PDF document
$pdf->Image('watermark.png', 10, 10, 100, 100);

// Set the font size and type of the watermark text
$pdf->SetFont('helvetica', '', 20);

// Set the color of the watermark text
$pdf->SetTextColor(255, 0, 0);

// Add the watermark text to the PDF document
$pdf->Cell(0, 0, 'Watermark Text', 0, 0, 'C');

// Output the PDF document
$pdf->Output('watermarked.pdf', 'I');

?>
```

## Helpful links
- [TCPDF Documentation](https://tcpdf.org/docs/srcdoc/index.html)
- [TCPDF Examples](https://tcpdf.org/examples/index.php)

onelinerhub: [How do I add a watermark to PDFs using PHP and TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-add-a-watermark-to-pdfs-using-php-and-tcpdf)