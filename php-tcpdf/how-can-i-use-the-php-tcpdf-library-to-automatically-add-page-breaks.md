# How can I use the PHP TCPDF library to automatically add page breaks?
// plain

You can use the PHP TCPDF library to automatically add page breaks by using the `addPageBreak()` method. This method will add a page break at the current position in the document.

## Example code

```
<?php
require_once('tcpdf_include.php');

$pdf = new TCPDF('P', 'mm', 'A4', true, 'UTF-8', false);

// add a page break
$pdf->addPageBreak();
?>
```

The code above will add a page break to an existing PDF document.

## Code explanation

- `require_once('tcpdf_include.php');` - This line includes the TCPDF library.
- `$pdf = new TCPDF('P', 'mm', 'A4', true, 'UTF-8', false);` - This line creates a new instance of the TCPDF class.
- `$pdf->addPageBreak();` - This line adds a page break at the current position in the document.

## Helpful links
- [TCPDF Documentation](https://tcpdf.org/docs/page-breaks/)
- [TCPDF GitHub Repository](https://github.com/tecnickcom/TCPDF)

onelinerhub: [How can I use the PHP TCPDF library to automatically add page breaks?](https://onelinerhub.com/php-tcpdf/how-can-i-use-the-php-tcpdf-library-to-automatically-add-page-breaks)