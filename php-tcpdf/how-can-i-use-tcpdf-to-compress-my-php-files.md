# How can I use TCPDF to compress my PHP files?
// plain

Using TCPDF to compress PHP files is a great way to reduce the size of your files and improve the speed of your website. The following example code will show you how to do this:

```
<?php
// Include the TCPDF library
require_once('tcpdf/tcpdf.php');

// Create a new instance of the TCPDF class
$pdf = new TCPDF();

// Compress the file
$pdf->setImageScale(PDF_IMAGE_SCALE_RATIO);

// Output the PDF
$pdf->Output('example.pdf', 'I');
?>
```

This code will create a new instance of the TCPDF class and then compress the file. The output of this code will be a PDF file called example.pdf.

## Code explanation

1. `require_once('tcpdf/tcpdf.php');` - This line includes the TCPDF library.
2. `$pdf = new TCPDF();` - This line creates a new instance of the TCPDF class.
3. `$pdf->setImageScale(PDF_IMAGE_SCALE_RATIO);` - This line compresses the file.
4. `$pdf->Output('example.pdf', 'I');` - This line outputs the PDF file named example.pdf.

## Helpful links
- [TCPDF Documentation](https://tcpdf.org/docs/index.php)
- [TCPDF Examples](https://tcpdf.org/examples/)

onelinerhub: [How can I use TCPDF to compress my PHP files?](https://onelinerhub.com/php-tcpdf/how-can-i-use-tcpdf-to-compress-my-php-files)