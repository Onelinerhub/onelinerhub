# How can I use a PHP variable to generate a PDF using TCPDF?
// plain

Using TCPDF to generate a PDF from a PHP variable is simple. First, you need to include the TCPDF library in your PHP code:

```
require_once('tcpdf/tcpdf.php');
```

Then, create a new instance of the TCPDF class:

```
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```

The parameters for the TCPDF constructor are:
* `PDF_PAGE_ORIENTATION` - the page orientation (`P` for portrait, `L` for landscape)
* `PDF_UNIT` - the unit of measure for the PDF document (`pt`, `mm`, `cm`, `in`)
* `PDF_PAGE_FORMAT` - the page format (`A4`, `A3`, etc.)
* `true` - boolean value that indicates if the document should be open in the browser
* `'UTF-8'` - the document encoding
* `false` - boolean value that indicates if the document should include the default header and footer

You can then use the `writeHTML()` method to add the contents of the PHP variable to the PDF document:

```
$pdf->writeHTML($php_variable);
```

Finally, you can use the `Output()` method to generate the PDF file:

```
$pdf->Output('my_file.pdf', 'I');
```

The parameters for the `Output()` method are:
* `my_file.pdf` - the name of the PDF file that will be generated
* `I` - the destination where the PDF will be sent (`I` for inline, `D` for download, `F` for file, `S` for string)

## Helpful links
* [TCPDF Documentation](https://tcpdf.org/docs.php)
* [TCPDF Examples](https://tcpdf.org/examples/)

onelinerhub: [How can I use a PHP variable to generate a PDF using TCPDF?](https://onelinerhub.com/php-tcpdf/how-can-i-use-a-php-variable-to-generate-a-pdf-using-tcpdf)