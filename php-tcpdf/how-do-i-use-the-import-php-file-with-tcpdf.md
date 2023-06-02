# How do I use the import.php file with TCPDF?
// plain

The `import.php` file is used with TCPDF to import existing PDF documents into a new PDF document. This is done by using the `TCPDF_IMPORT` class, which is included in the `import.php` file.

Example code to import a PDF into a new PDF document:
```
<?php
// Include the import.php file
require_once('import.php');

// Create a new TCPDF object
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// Import the PDF document
$pdf->setSourceFile('example.pdf');
$tplIdx = $pdf->importPage(1);

// Add the imported page to the new PDF document
$pdf->addPage();
$pdf->useTemplate($tplIdx, 10, 10, 90);

// Output the new PDF document
$pdf->Output('example_imported.pdf', 'I');
```

This code will create a new PDF document and import the first page of the `example.pdf` document into it. The imported page will be placed at the top-left corner of the new PDF document, with a 10 pt margin on each side. The new PDF document will be outputted as `example_imported.pdf`.

## Code explanation


1. Include the `import.php` file: `require_once('import.php');`
2. Create a new TCPDF object: `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);`
3. Import the PDF document: `$pdf->setSourceFile('example.pdf'); $tplIdx = $pdf->importPage(1);`
4. Add the imported page to the new PDF document: `$pdf->addPage(); $pdf->useTemplate($tplIdx, 10, 10, 90);`
5. Output the new PDF document: `$pdf->Output('example_imported.pdf', 'I');`

## Helpful links

- [TCPDF Documentation](https://tcpdf.org/docs/srcdoc/class-TCPDF/#_import_page)
- [TCPDF Examples](https://tcpdf.org/examples/example_018/)

onelinerhub: [How do I use the import.php file with TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-use-the-import-php-file-with-tcpdf)