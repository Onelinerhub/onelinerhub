# How do I use the TCPDF PHP library to generate PDF documents?
// plain

Using the TCPDF library for generating PDF documents is quite easy. It requires a few simple steps:

1. Include the TCPDF library in your project:
```php
require_once('tcpdf_include.php');
```

2. Create a new TCPDF object:
```php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```

3. Set the document information:
```php
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Author Name');
$pdf->SetTitle('Document Title');
$pdf->SetSubject('Document Subject');
$pdf->SetKeywords('keyword1, keyword2');
```

4. Add a page:
```php
$pdf->AddPage();
```

5. Generate the PDF content:
```php
$pdf->writeHTML('<h1>Hello World!</h1>', true, false, true, false, '');
```

6. Output the generated PDF:
```php
$pdf->Output('document.pdf', 'I');
```

7. Finally, you can also use the TCPDF library to create complex PDF documents with images, tables, etc.

## Helpful links
- [TCPDF Documentation](https://tcpdf.org/docs.php)
- [TCPDF Examples](https://tcpdf.org/examples/)

onelinerhub: [How do I use the TCPDF PHP library to generate PDF documents?](https://onelinerhub.com/php-tcpdf/how-do-i-use-the-tcpdf-php-library-to-generate-pdf-documents)