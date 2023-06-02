# How can I use TCPDF with PHP?
// plain

Using TCPDF with PHP is fairly straightforward. First, you need to include the TCPDF library in your project by downloading it from the [TCPDF website](https://tcpdf.org/). Then, you can create a new instance of the TCPDF class with the following code block:

```php
require_once('tcpdf_include.php');
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```

The parameters of the constructor are as follows:
- `PDF_PAGE_ORIENTATION`: The orientation of the page. Possible values are `PDF_PAGE_ORIENTATION_P` for portrait or `PDF_PAGE_ORIENTATION_L` for landscape.
- `PDF_UNIT`: The unit of measure. Possible values are `PDF_UNIT_PT` for points, `PDF_UNIT_MM` for millimeters, `PDF_UNIT_CM` for centimeters, `PDF_UNIT_IN` for inches.
- `PDF_PAGE_FORMAT`: The size of the page. Possible values are `PDF_PAGE_FORMAT_A4`, `PDF_PAGE_FORMAT_LETTER`, etc.
- `true`: Boolean indicating if the document should open in full screen mode when opened.
- `'UTF-8'`: The document's encoding.
- `false`: Boolean indicating if the document should be compressed.

Once the instance is created, you can use the available methods to add content to the document. For example, to add a page and some text to the document, you can use the following code:

```php
$pdf->AddPage();
$pdf->Write(0, 'Hello world!', '', 0, 'L', true, 0, false, false, 0);
```

The parameters of the `Write` method are as follows:
- `0`: The cell height.
- `'Hello world!'`: The string to print.
- `''`: The link.
- `0`: The x position of the cell.
- `'L'`: The cell alignment. Possible values are `L` for left, `C` for center, `R` for right, `J` for justified.
- `true`: Boolean indicating if the cell should be filled or not.
- `0`: The border.
- `false`: Boolean indicating if the cell should have a bottom border or not.
- `false`: Boolean indicating if the cell should have a left border or not.
- `0`: The cell padding.

Finally, the document can be outputted with the `Output` method.

```php
$pdf->Output('example.pdf', 'I');
```

The parameters of the `Output` method are as follows:
- `'example.pdf'`: The name of the file.
- `'I'`: The output destination. Possible values are `I` for inline, `D` for download, `F` for file, `S` for string.

For more information on how to use TCPDF with PHP, please refer to the [TCPDF documentation](https://tcpdf.org/docs/).

onelinerhub: [How can I use TCPDF with PHP?](https://onelinerhub.com/php-tcpdf/how-can-i-use-tcpdf-with-php)