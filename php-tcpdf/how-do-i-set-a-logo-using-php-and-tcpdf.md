# How do I set a logo using PHP and TCPDF?
// plain

Using TCPDF and PHP you can set a logo on your PDF document. The following example code will show you how to do this:

```
<?php

// Include the TCPDF library
require_once('tcpdf_include.php');

// Create a new TCPDF object
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// Set the logo
$logo = 'logo.png';
$pdf->Image($logo, 10, 10, 15, '', 'PNG', '', 'T', false, 300, '', false, false, 0, false, false, false);

// Output the PDF
$pdf->Output('example.pdf', 'I');

?>
```

The code above will output a PDF with a logo at the top left corner. The code is split into the following parts:

1. Include the TCPDF library - `require_once('tcpdf_include.php');`
2. Create a new TCPDF object - `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);`
3. Set the logo - `$pdf->Image($logo, 10, 10, 15, '', 'PNG', '', 'T', false, 300, '', false, false, 0, false, false, false);`
4. Output the PDF - `$pdf->Output('example.pdf', 'I');`

For more information on how to use TCPDF and PHP to set a logo, you can refer to the [TCPDF Documentation](https://tcpdf.org/examples/example_011/) and the [TCPDF Image Method](https://tcpdf.org/docs/classTCPDF/#image).

onelinerhub: [How do I set a logo using PHP and TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-set-a-logo-using-php-and-tcpdf)