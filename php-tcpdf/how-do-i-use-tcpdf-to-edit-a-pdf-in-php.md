# How do I use TCPDF to edit a PDF in PHP?
// plain

TCPDF is a powerful PHP library for creating and editing PDF documents. It is a free and open source library, and is easy to use with a few simple steps.

To use TCPDF to edit a PDF in PHP, you first need to include the TCPDF library in your script.

```php
require_once('tcpdf/tcpdf.php');
```

Then, create a new instance of the TCPDF class, and set the document properties.

```php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Author Name');
$pdf->SetTitle('My Document');
$pdf->SetSubject('My Subject');
$pdf->SetKeywords('TCPDF, PDF, example, test, guide');

// No output
```

Then, you can add content to the PDF document with the `AddPage()` and `writeHTML()` methods.

```php
// Add a page
$pdf->AddPage();

// Set some content to print
$html = <<<EOD
<h1>My Document</h1>
<p>This is my PDF document.</p>
EOD;

// Print text using writeHTMLCell()
$pdf->writeHTMLCell(0, 0, '', '', $html, 0, 1, 0, true, '', true);

// No output
```

Finally, you can save or output the PDF document with the `Output()` or `Output('file.pdf', 'F')` methods.

```php
$pdf->Output('file.pdf', 'F');

// Outputs the PDF document to a file
```

You can find more information about using TCPDF to edit PDF documents in the [TCPDF Documentation](https://tcpdf.org/docs/).

onelinerhub: [How do I use TCPDF to edit a PDF in PHP?](https://onelinerhub.com/php-tcpdf/how-do-i-use-tcpdf-to-edit-a-pdf-in-php)