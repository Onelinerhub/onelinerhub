# How do I use the TCPDF Arial.php file?
// plain

Using the TCPDF Arial.php file is a great way to generate PDF documents with the Arial font. To use it, you first need to include the file in your PHP program:

```
require_once('tcpdf_arial.php');
```

Then you can create a new instance of the TCPDF class and set the font to Arial:

```
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
$pdf->SetFont('arial', '', 10);
```

You can then use the `Write()` method to write text to the PDF document:

```
$pdf->Write(0, 'Hello World', '', 0, 'L', true, 0, false, false, 0);
```

The `Write()` method has the following parts:

1. `$h`: The line height.
2. `$txt`: The text to be written.
3. `$link`: An optional link.
4. `$fill`: Indicates if the cell background must be painted (1) or transparent (0).
5. `$align`: The text alignment. Possible values are:
    * `L` or empty string: left alignment
    * `C`: center alignment
    * `R`: right alignment
6. `$ln`: Indicates if a new line should be added after the text (true) or not (false).
7. `$stretch`: Stretch carachter mode.
8. `$firstline`: if true prints only the first line and return the remaining string.
9. `$firstblock`: if true the string is always wrapped on the first block (strlen($txt) < $width).

You can find more information about the TCPDF Arial.php file in the [TCPDF documentation](https://tcpdf.org/docs/source_docs/classTCPDF/#a9a3b09e8e4f8d972f8a77e6b1c8d09e).

For more examples of using TCPDF, see the [examples page](https://tcpdf.org/examples/).

onelinerhub: [How do I use the TCPDF Arial.php file?](https://onelinerhub.com/php-tcpdf/how-do-i-use-the-tcpdf-arial-php-file)