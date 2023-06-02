# How can I use PHP to generate a PDF document with HTML content?
// plain

Using PHP to generate a PDF document with HTML content is relatively simple. You can use the [FPDF](http://www.fpdf.org/) library for this purpose.

The following example code will generate a PDF document with HTML content:

```php
// Include the FPDF library
require('fpdf.php');

// Create a new instance of the FPDF class
$pdf = new FPDF();

// Set the document title
$pdf->SetTitle('My PDF Document');

// Add a page to the document
$pdf->AddPage();

// Set the font
$pdf->SetFont('Arial', 'B', 16);

// Write the HTML content
$pdf->WriteHTML('<h1>My PDF Document</h1>');
$pdf->WriteHTML('<p>This is a sample PDF document with HTML content.</p>');

// Output the document
$pdf->Output('my_pdf_document.pdf', 'I');
```

This code will generate a PDF document with the title "My PDF Document" and the following content:

```
My PDF Document

This is a sample PDF document with HTML content.
```

The code consists of the following parts:

1. Include the FPDF library: `require('fpdf.php');`
2. Create a new instance of the FPDF class: `$pdf = new FPDF();`
3. Set the document title: `$pdf->SetTitle('My PDF Document');`
4. Add a page to the document: `$pdf->AddPage();`
5. Set the font: `$pdf->SetFont('Arial', 'B', 16);`
6. Write the HTML content: `$pdf->WriteHTML('<h1>My PDF Document</h1>');`
7. Output the document: `$pdf->Output('my_pdf_document.pdf', 'I');`

For more information, see the [FPDF website](http://www.fpdf.org/).

onelinerhub: [How can I use PHP to generate a PDF document with HTML content?](https://onelinerhub.com/php-tcpdf/how-can-i-use-php-to-generate-a-pdf-document-with-html-content)