# How do I use the PHP TCPDF Kernel to generate PDFs?
// plain

To use the PHP TCPDF Kernel to generate PDFs, the following steps must be followed:
1. Include the TCPDF library in your PHP script.
```php
require_once('tcpdf_include.php');
```

2. Create a new instance of the TCPDF class.
```php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```

3. Set the document information.
```php
// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('John Doe');
$pdf->SetTitle('My PDF Document');
$pdf->SetSubject('TCPDF Tutorial');
$pdf->SetKeywords('TCPDF, PDF, example, test, guide');
```

4. Set the header and footer.
```php
// set header and footer fonts
$pdf->setHeaderFont(Array(PDF_FONT_NAME_MAIN, '', PDF_FONT_SIZE_MAIN));
$pdf->setFooterFont(Array(PDF_FONT_NAME_DATA, '', PDF_FONT_SIZE_DATA));

// set margins
$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);
$pdf->SetHeaderMargin(PDF_MARGIN_HEADER);
$pdf->SetFooterMargin(PDF_MARGIN_FOOTER);
```

5. Add content to the document.
```php
// set font
$pdf->SetFont('helvetica', 'B', 20);

// add a page
$pdf->AddPage();

// write some HTML code
$pdf->Write(0, 'Hello World!');
```

6. Generate the PDF document.
```php
$pdf->Output('example_001.pdf', 'I');
```

7. Output the generated PDF document.
```
example_001.pdf
```

## Helpful links
- [TCPDF Documentation](http://www.tcpdf.org/doc/code/classTCPDF.html)
- [TCPDF Examples](https://tcpdf.org/examples/)

onelinerhub: [How do I use the PHP TCPDF Kernel to generate PDFs?](https://onelinerhub.com/php-tcpdf/how-do-i-use-the-php-tcpdf-kernel-to-generate-pdfs)