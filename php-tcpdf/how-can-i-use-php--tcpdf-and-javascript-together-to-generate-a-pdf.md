# How can I use PHP, TCPDF and JavaScript together to generate a PDF?
// plain

You can use PHP, TCPDF and JavaScript together to generate a PDF by creating a PDF document using TCPDF and then adding JavaScript to it. To do this, you can use the TCPDF class to create a new PDF document, then use the `addJavascript()` method to add JavaScript to the document.

```php
// Include the TCPDF library
require_once('tcpdf_include.php');

// Create a new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// Add JavaScript to the document
$js = 'function myFunction() { alert("Hello World!"); }';
$pdf->addJavascript($js);

// Output the document
$pdf->Output('example.pdf', 'I');
```

The code above will generate a PDF document with a JavaScript function called `myFunction()` that will display an alert when the document is opened.

The following parts are involved in the code above:

- `require_once('tcpdf_include.php')`: this includes the TCPDF library, which is necessary for working with PDF documents.
- `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false)`: this creates a new PDF document using the TCPDF class.
- `$js = 'function myFunction() { alert("Hello World!"); }'`: this creates a JavaScript string containing a function called `myFunction()`.
- `$pdf->addJavascript($js)`: this adds the JavaScript string to the PDF document.
- `$pdf->Output('example.pdf', 'I')`: this outputs the PDF document to the browser.

## Helpful links

- [TCPDF Documentation](https://tcpdf.org/docs.php)
- [PHP Manual: TCPDF](https://www.php.net/manual/en/book.tcpdf.php)

onelinerhub: [How can I use PHP, TCPDF and JavaScript together to generate a PDF?](https://onelinerhub.com/php-tcpdf/how-can-i-use-php--tcpdf-and-javascript-together-to-generate-a-pdf)