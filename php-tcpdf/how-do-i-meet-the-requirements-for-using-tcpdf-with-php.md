# How do I meet the requirements for using TCPDF with PHP?
// plain

To use TCPDF with PHP, you need to include the TCPDF library in your project. This can be done by downloading the source code from their [GitHub repository](https://github.com/tecnickcom/TCPDF) and adding it to your project.

Once the library is included, you need to create an instance of the TCPDF class. This is done by instantiating the class with the `new` keyword, like so:

```php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```

The parameters for the constructor are:
* `PDF_PAGE_ORIENTATION`: The page orientation (`P` or `L` for portrait or landscape, respectively).
* `PDF_UNIT`: The unit of measure for the document (`pt`, `mm`, `cm`, `in`).
* `PDF_PAGE_FORMAT`: The page format (`A4`, `A3`, etc.).
* `true`: Boolean value that tells the library to automatically generate the page header and footer.
* `'UTF-8'`: The document encoding.
* `false`: Boolean value that tells the library not to compress the output.

You can then use the `AddPage()` method to add a page to the document, and the `WriteHTML()` method to write HTML content to the page:

```php
$pdf->AddPage();
$html = '<h1>Hello, world!</h1>';
$pdf->WriteHTML($html);
```

Finally, you can output the PDF document using the `Output()` method:

```php
$pdf->Output('example.pdf', 'I');
```

The parameters for the `Output()` method are:
* `'example.pdf'`: The name of the file to output.
* `'I'`: The output mode (`I` for inline, `D` for download, `F` for file, `S` for string).

For more information on using TCPDF, see the [documentation](https://tcpdf.org/docs/).

onelinerhub: [How do I meet the requirements for using TCPDF with PHP?](https://onelinerhub.com/php-tcpdf/how-do-i-meet-the-requirements-for-using-tcpdf-with-php)