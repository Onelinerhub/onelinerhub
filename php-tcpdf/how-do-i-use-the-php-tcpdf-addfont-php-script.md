# How do I use the php tcpdf_addfont.php script?
// plain

The php tcpdf_addfont.php script is used to add new fonts to the TCPDF library. It can be used as follows:

1. Download the font file (e.g. .ttf or .otf) that you want to add to the TCPDF library.

2. Place the font file in the tcpdf/fonts folder.

3. Execute the php tcpdf_addfont.php script with the font file as an argument.

For example, to add a font called 'myfont.ttf':

```
php tcpdf_addfont.php myfont.ttf
```

This will generate a .php file for the font (e.g. myfont.php).

4. Include this .php file in your code.

```
require_once('tcpdf/fonts/myfont.php');
```

5. Set the font in the TCPDF instance.

```
$pdf->SetFont('myfont', '', 14, '', false);
```

6. Use the font as you would any other font in the TCPDF library.

7. Save and output the PDF file.

## Helpful links

- [TCPDF Fonts](https://tcpdf.org/fonts/): Documentation on how to add fonts to the TCPDF library
- [TCPDF Examples](https://tcpdf.org/examples/): Examples on how to use TCPDF with various fonts

onelinerhub: [How do I use the php tcpdf_addfont.php script?](https://onelinerhub.com/php-tcpdf/how-do-i-use-the-php-tcpdf-addfont-php-script)