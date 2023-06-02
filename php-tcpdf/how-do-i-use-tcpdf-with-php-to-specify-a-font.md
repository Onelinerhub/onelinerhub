# How do I use TCPDF with PHP to specify a font?
// plain

Using TCPDF with PHP to specify a font is easy. First, you need to include the TCPDF library in your project.

```
<?php
require_once('tcpdf_include.php');
?>
```

Then you need to create a new TCPDF object.

```
<?php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
?>
```

After that you can use the `SetFont()` method to specify a font.

```
<?php
$pdf->SetFont('dejavusans', '', 14, '', true);
?>
```

The first parameter is the font family. The second parameter is the font style (e.g. 'B' for bold). The third parameter is the font size. The fourth parameter is the font file path (if the font is not in the TCPDF folder). The fifth parameter is a boolean value that indicates whether the font is embedded or not.

You can also use the `AddFont()` method to add a custom font.

```
<?php
$fontname = $pdf->AddFont('myfont', '', 'myfont.php');
$pdf->SetFont($fontname, '', 14, '', true);
?>
```

The first parameter is the font family name. The second parameter is the font style (e.g. 'B' for bold). The third parameter is the font file path.

For more information, please refer to the [TCPDF documentation](https://tcpdf.org/docs/source-docs/classTCPDF/#a8e9e7b9d0d3b9d3e4e4f2f4f0b2f7a5).

onelinerhub: [How do I use TCPDF with PHP to specify a font?](https://onelinerhub.com/php-tcpdf/how-do-i-use-tcpdf-with-php-to-specify-a-font)