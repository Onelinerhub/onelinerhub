# How can I use TCPDF with PHP on GitHub?
// plain

To use TCPDF with PHP on GitHub, you need to first install the TCPDF library. You can do this by cloning the repo from GitHub using the following command:
```
git clone https://github.com/tecnickcom/TCPDF
```

Once the repo is cloned, you can include the TCPDF library in your PHP script using the following code:
```php
require_once('/path/to/TCPDF/tcpdf.php');
```

You can then create a new instance of the TCPDF class and use its various methods to generate PDF documents. For example, the following code will create a new PDF document and save it to a file:
```php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
$pdf->AddPage();
$pdf->writeHTML('<h1>Hello World!</h1>', true, false, true, false, '');
$pdf->Output('hello_world.pdf', 'F');
```

The above code will create a PDF document with the heading "Hello World!" and save it to a file called hello_world.pdf.

The TCPDF library also provides a number of other methods that can be used to generate PDF documents, such as adding images, tables, and text. You can find more information about these methods in the [TCPDF documentation](https://tcpdf.org/).

**## Helpful links**
- [TCPDF GitHub repo](https://github.com/tecnickcom/TCPDF)
- [TCPDF documentation](https://tcpdf.org/)

onelinerhub: [How can I use TCPDF with PHP on GitHub?](https://onelinerhub.com/php-tcpdf/how-can-i-use-tcpdf-with-php-on-github)