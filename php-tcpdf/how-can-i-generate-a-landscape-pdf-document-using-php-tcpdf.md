# How can I generate a landscape PDF document using PHP TCPDF?
// plain

Generating a landscape PDF document using PHP TCPDF can be done in a few simple steps.

1. Include the TCPDF library in your PHP file:
```
require_once('tcpdf/tcpdf.php');
```
2. Create a new instance of TCPDF:
```
$pdf = new TCPDF('L', PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```
3. Set the document information:
```
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Your Name');
$pdf->SetTitle('My PDF Document');
$pdf->SetSubject('My Subject');
$pdf->SetKeywords('keywords, here');
```
4. Set the default header data:
```
$pdf->SetHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING, array(0,64,255), array(0,64,128));
```
5. Set the margins:
```
$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);
```
6. Set auto page breaks:
```
$pdf->SetAutoPageBreak(TRUE, PDF_MARGIN_BOTTOM);
```
7. Add a page:
```
$pdf->AddPage();
```

Once these steps are complete, you can then add content to the PDF document using the TCPDF methods, such as `MultiCell()`, `WriteHTML()`, etc.

## Helpful links
- [TCPDF Documentation](https://tcpdf.org/docs/index.php)
- [TCPDF Examples](https://tcpdf.org/examples/)

onelinerhub: [How can I generate a landscape PDF document using PHP TCPDF?](https://onelinerhub.com/php-tcpdf/how-can-i-generate-a-landscape-pdf-document-using-php-tcpdf)