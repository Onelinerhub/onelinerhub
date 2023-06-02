# How do I use fonts in PHP TCPDF?
// plain

To use fonts in PHP TCPDF, you can do the following:

1. Download the desired font file from the [TCPDF font repository](https://tcpdf.org/fonts/)
2. Extract the font file from the compressed file
3. Add the font file to the `tcpdf/fonts` directory
4. Add the following code to the `tcpdf_config.php` file

```php
<?php
$fontname = TCPDF_FONTS::addTTFfont('/path/to/font/file', 'TrueTypeUnicode', '', 96);
```

5. Use the font in the PDF document

```php
<?php
$pdf->SetFont($fontname, '', 14, '', false);
```

6. Generate the PDF document

```php
<?php
$pdf->Output('example.pdf', 'I');
```

7. The PDF document will be generated with the specified font.

onelinerhub: [How do I use fonts in PHP TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-use-fonts-in-php-tcpdf)