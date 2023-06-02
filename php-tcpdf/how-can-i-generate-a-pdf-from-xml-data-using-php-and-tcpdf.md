# How can I generate a PDF from XML data using PHP and TCPDF?
// plain

Generating a PDF from XML data using PHP and TCPDF is a relatively straightforward process. The following example code block will demonstrate how to do this:
```php
<?php
// Include the TCPDF library
require_once('tcpdf_include.php');

// Create a new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// Load the XML data
$xml = simplexml_load_file('data.xml');

// Set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Author Name');
$pdf->SetTitle('Document Title');

// Add a page
$pdf->AddPage();

// Output the XML data
foreach ($xml->data as $data) {
    $pdf->Write(0, $data->name.' - '.$data->email);
}

// Output the PDF document
$pdf->Output('document.pdf', 'I');
```

The code above will generate a PDF document containing the XML data. It consists of the following parts:

1. Include the TCPDF library: This is done with the `require_once` function, which will include the TCPDF library in the script.

2. Create a new PDF document: This is done with the `TCPDF` class, which will create a new PDF document with the specified parameters.

3. Load the XML data: This is done with the `simplexml_load_file` function, which will load the XML data from a file.

4. Set document information: This is done with the `SetCreator`, `SetAuthor` and `SetTitle` methods, which will set the document information.

5. Add a page: This is done with the `AddPage` method, which will add a new page to the document.

6. Output the XML data: This is done with the `Write` method, which will output the XML data to the PDF.

7. Output the PDF document: This is done with the `Output` method, which will output the PDF document to the browser.

## Helpful links
- [TCPDF Library](https://tcpdf.org/)
- [simplexml_load_file](https://www.php.net/manual/en/function.simplexml-load-file.php)

onelinerhub: [How can I generate a PDF from XML data using PHP and TCPDF?](https://onelinerhub.com/php-tcpdf/how-can-i-generate-a-pdf-from-xml-data-using-php-and-tcpdf)