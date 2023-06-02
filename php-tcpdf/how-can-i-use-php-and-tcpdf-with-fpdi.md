# How can I use PHP and TCPDF with FPDI?
// plain

PHP and TCPDF can be used together with FPDI to create PDF documents from existing PDF documents.

First, you need to install and include the necessary libraries in your project:

```php
require_once('fpdf/fpdf.php');
require_once('fpdi/fpdi.php');
require_once('tcpdf/tcpdf.php');
```

Then, create an instance of the FPDI class and set the source PDF document:

```php
$pdf = new FPDI();
$pdf->setSourceFile('source.pdf');
```

After that, you can import the page from the source document and add content to it:

```php
$pageId = $pdf->importPage(1);
$pdf->useTemplate($pageId);
$pdf->SetFont('Arial');
$pdf->SetTextColor(255, 0, 0);
$pdf->SetXY(20, 20);
$pdf->Write(0, 'Hello World!');
```

Finally, you can output the PDF document using the TCPDF class:

```php
$pdf = new TCPDF();
$pdf->AddPage();
$pdf->writeHTML($pdf->Output('', 'S'));
$pdf->Output('example.pdf', 'D');
```

The example code will create a new PDF document with the content imported from the source document and the text "Hello World!" added to it.

Parts of the code:

1. Require the necessary libraries - `require_once('fpdf/fpdf.php'); require_once('fpdi/fpdi.php'); require_once('tcpdf/tcpdf.php');`
2. Create an instance of the FPDI class and set the source PDF document - `$pdf = new FPDI(); $pdf->setSourceFile('source.pdf');`
3. Import the page from the source document and add content to it - `$pageId = $pdf->importPage(1); $pdf->useTemplate($pageId); $pdf->SetFont('Arial'); $pdf->SetTextColor(255, 0, 0); $pdf->SetXY(20, 20); $pdf->Write(0, 'Hello World!');`
4. Output the PDF document using the TCPDF class - `$pdf = new TCPDF(); $pdf->AddPage(); $pdf->writeHTML($pdf->Output('', 'S')); $pdf->Output('example.pdf', 'D');`

## Helpful links

- [FPDI Documentation](https://www.setasign.com/products/fpdi/manual/index.html)
- [TCPDF Documentation](https://tcpdf.org/docs.php)

onelinerhub: [How can I use PHP and TCPDF with FPDI?](https://onelinerhub.com/php-tcpdf/how-can-i-use-php-and-tcpdf-with-fpdi)