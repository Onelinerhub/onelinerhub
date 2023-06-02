# How do I use TCPDF with PHP?
// plain

Using TCPDF with PHP is easy and straightforward. To get started, you need to include the TCPDF library in your project.

```
require_once('tcpdf_include.php');
```

Next, create an instance of the TCPDF class and set the page size, orientation, and margins.

```
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);
```

Then, you can add content to the PDF document using the `writeHTML()` method.

```
$html = '<h1>Hello World!</h1>';
$pdf->writeHTML($html, true, false, true, false, '');
```

Finally, you can output the PDF document using the `Output()` method.

```
$pdf->Output('example.pdf', 'I');
```

The code above will generate a PDF document with the following output:

```
Hello World!
```

Here is a list of useful methods for working with TCPDF:

* `SetMargins()` - Sets the page margins.
* `AddPage()` - Adds a new page to the document.
* `SetFont()` - Sets the font used for the document.
* `WriteHTML()` - Writes HTML code to the document.
* `Output()` - Outputs the document to the browser or a file.

For more information, see the [TCPDF documentation](https://tcpdf.org/docs/).

onelinerhub: [How do I use TCPDF with PHP?](https://onelinerhub.com/php-tcpdf/how-do-i-use-tcpdf-with-php)