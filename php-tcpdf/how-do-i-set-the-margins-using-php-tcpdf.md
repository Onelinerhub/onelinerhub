# How do I set the margins using PHP TCPDF?
// plain

Using the PHP TCPDF library, you can easily set the margins of your document. The following example code block sets the left, top, right, and bottom margins to 20 mm each:

```
<?php

// Include the library
require_once('tcpdf_include.php');

// Create a new instance of TCPDF
$pdf = new TCPDF();

// Set the margins
$pdf->SetMargins(20, 20, 20, 20);

// Output the document
$pdf->Output('example.pdf', 'I');

?>
```

This code will create a document with 20 mm margins on all four sides.

## Code explanation


1. `require_once('tcpdf_include.php')` - This line includes the TCPDF library.
2. `$pdf = new TCPDF()` - This line creates a new instance of TCPDF.
3. `$pdf->SetMargins(20, 20, 20, 20)` - This line sets the left, top, right, and bottom margins to 20 mm each.
4. `$pdf->Output('example.pdf', 'I')` - This line outputs the document to a file named example.pdf.

For more information about setting margins with TCPDF, see the [TCPDF documentation](http://www.tcpdf.org/doc/code/classTCPDF.html#a7f5b8e7f45f8b3a6a4f2f8e18d2a2d5b).

onelinerhub: [How do I set the margins using PHP TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-set-the-margins-using-php-tcpdf)