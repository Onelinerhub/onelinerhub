# How can I use Yandex with PHP TCPDF?
// plain

You can use Yandex with PHP TCPDF to generate PDF documents from HTML. The following example shows how to use Yandex with PHP TCPDF:

```
require_once('tcpdf/tcpdf.php');
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
$pdf->SetDefaultMonospacedFont(PDF_FONT_MONOSPACED);
$pdf->SetHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING, array(0,64,255), array(0,64,128));
$pdf->setFooterData(array(0,64,0), array(0,64,128));
$pdf->SetHeaderMargin(PDF_MARGIN_HEADER);
$pdf->SetFooterMargin(PDF_MARGIN_FOOTER);
$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);
$pdf->SetAutoPageBreak(TRUE, PDF_MARGIN_BOTTOM);
$pdf->setImageScale(PDF_IMAGE_SCALE_RATIO);
$pdf->SetFont('dejavusans', '', 10);
$pdf->AddPage();
$html = '<h1>Yandex with PHP TCPDF</h1>';
$pdf->writeHTML($html, true, false, true, false, '');
$pdf->Output('example_001.pdf', 'I');
```

This code creates a PDF document with a title of "Yandex with PHP TCPDF".

The code consists of the following parts:

1. Require the TCPDF library: `require_once('tcpdf/tcpdf.php');`
2. Create a new TCPDF object: `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);`
3. Set the default font: `$pdf->SetDefaultMonospacedFont(PDF_FONT_MONOSPACED);`
4. Set the header and footer data: `$pdf->SetHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING, array(0,64,255), array(0,64,128));`
5. Set the header and footer margins: `$pdf->SetHeaderMargin(PDF_MARGIN_HEADER); $pdf->SetFooterMargin(PDF_MARGIN_FOOTER);`
6. Set the page margins: `$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);`
7. Set the auto page break: `$pdf->SetAutoPageBreak(TRUE, PDF_MARGIN_BOTTOM);`
8. Set the image scale ratio: `$pdf->setImageScale(PDF_IMAGE_SCALE_RATIO);`
9. Set the font: `$pdf->SetFont('dejavusans', '', 10);`
10. Add a page: `$pdf->AddPage();`
11. Create the HTML content: `$html = '<h1>Yandex with PHP TCPDF</h1>';`
12. Write the HTML content to the PDF document: `$pdf->writeHTML($html, true, false, true, false, '');`
13. Output the PDF document: `$pdf->Output('example_001.pdf', 'I');`

For more information on using Yandex with PHP TCPDF, see the [TCPDF documentation](https://tcpdf.org/).

onelinerhub: [How can I use Yandex with PHP TCPDF?](https://onelinerhub.com/php-tcpdf/how-can-i-use-yandex-with-php-tcpdf)