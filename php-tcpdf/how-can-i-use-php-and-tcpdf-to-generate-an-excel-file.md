# How can I use PHP and TCPDF to generate an Excel file?
// plain

You can use PHP and TCPDF to generate an Excel file by using the TCPDF_FILTERS class to convert the PDF file into an Excel file. For example:

```
// Include the TCPDF library
require_once('tcpdf_include.php');

// Create a new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// Set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetTitle('My Excel File');

// Set the default font
$pdf->SetFont('helvetica', '', 12);

// Add a page
$pdf->AddPage();

// Add some content to the document
$pdf->Write(0, 'Hello World!', '', 0, 'L', true, 0, false, false, 0);

// Close and output the PDF document
$pdf->Output('MyExcelFile.xls', 'F');
```

This code will generate an Excel file, named 'MyExcelFile.xls'.

## Code explanation


- `require_once('tcpdf_include.php');` - this line includes the TCPDF library, which is necessary for generating the Excel file.

- `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);` - this line creates a new PDF document, with the specified page orientation, unit and format.

- `$pdf->SetCreator(PDF_CREATOR);` - this line sets the document creator.

- `$pdf->SetTitle('My Excel File');` - this line sets the document title.

- `$pdf->SetFont('helvetica', '', 12);` - this line sets the default font.

- `$pdf->AddPage();` - this line adds a page to the document.

- `$pdf->Write(0, 'Hello World!', '', 0, 'L', true, 0, false, false, 0);` - this line adds some content to the document.

- `$pdf->Output('MyExcelFile.xls', 'F');` - this line outputs the PDF document as an Excel file, named 'MyExcelFile.xls'.

## Helpful links

- [TCPDF Library](https://tcpdf.org/)
- [TCPDF_FILTERS Class](https://tcpdf.org/docs/class-TCPDF_FILTERS.html)

onelinerhub: [How can I use PHP and TCPDF to generate an Excel file?](https://onelinerhub.com/php-tcpdf/how-can-i-use-php-and-tcpdf-to-generate-an-excel-file)