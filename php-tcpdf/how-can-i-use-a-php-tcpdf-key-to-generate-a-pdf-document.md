# How can I use a PHP TCPDF key to generate a PDF document?
// plain

The PHP TCPDF library is an open source library for generating PDF documents. It can be used to generate PDF documents from HTML, text, and images.

To generate a PDF document using the PHP TCPDF library, you will need to include the TCPDF library in your project and create a new instance of the TCPDF class.

```php
require_once('tcpdf_include.php');

$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```

Once the instance of the TCPDF class is created, you can set the document properties, add page headers and footers, and add content to the document.

```php
// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetTitle('My PDF Document');

// set default header data
$pdf->SetHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING);

// set header and footer fonts
$pdf->setHeaderFont(Array(PDF_FONT_NAME_MAIN, '', PDF_FONT_SIZE_MAIN));
$pdf->setFooterFont(Array(PDF_FONT_NAME_DATA, '', PDF_FONT_SIZE_DATA));

// add a page
$pdf->AddPage();

// write some HTML code
$html = '<h1>My PDF Document</h1>
<p>This is my PDF document.</p>';

// output the HTML content
$pdf->writeHTML($html, true, false, true, false, '');
```

Finally, you can output the PDF document to the browser or save it to a file.

```php
// output the PDF document
$pdf->Output('my_pdf_document.pdf', 'I');
```

Parts of the code:

1. `require_once('tcpdf_include.php');` - including the TCPDF library in the project.
2. `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);` - creating a new instance of the TCPDF class.
3. `$pdf->SetCreator(PDF_CREATOR);` - setting the document creator.
4. `$pdf->SetTitle('My PDF Document');` - setting the document title.
5. `$pdf->SetHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING);` - setting the header data.
6. `$pdf->setHeaderFont(Array(PDF_FONT_NAME_MAIN, '', PDF_FONT_SIZE_MAIN));` - setting the header font.
7. `$pdf->setFooterFont(Array(PDF_FONT_NAME_DATA, '', PDF_FONT_SIZE_DATA));` - setting the footer font.
8. `$pdf->AddPage();` - adding a page.
9. `$html = '<h1>My PDF Document</h1>
<p>This is my PDF document.</p>';` - writing some HTML code.
10. `$pdf->writeHTML($html, true, false, true, false, '');` - outputting the HTML content.
11. `$pdf->Output('my_pdf_document.pdf', 'I');` - outputting the PDF document.

## Helpful links

- [PHP TCPDF Library](https://tcpdf.org/)
- [TCPDF Documentation](https://tcpdf.org/docs.php)

onelinerhub: [How can I use a PHP TCPDF key to generate a PDF document?](https://onelinerhub.com/php-tcpdf/how-can-i-use-a-php-tcpdf-key-to-generate-a-pdf-document)