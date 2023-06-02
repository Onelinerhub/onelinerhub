# How can I add a footer to a PDF generated using PHP and TCPDF?
// plain

Using the TCPDF library, you can add a footer to a PDF generated with PHP. The following example code block shows how to do this:

```
// create new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Author Name');
$pdf->SetTitle('My PDF Title');
$pdf->SetSubject('My PDF Subject');
$pdf->SetKeywords('TCPDF, PDF, example, test, guide');

// set default header data
$pdf->SetHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING, array(0,64,255), array(0,64,128));
$pdf->setFooterData(array(0,64,0), array(0,64,128));

// set header and footer fonts
$pdf->setHeaderFont(Array(PDF_FONT_NAME_MAIN, '', PDF_FONT_SIZE_MAIN));
$pdf->setFooterFont(Array(PDF_FONT_NAME_DATA, '', PDF_FONT_SIZE_DATA));

// set default monospaced font
$pdf->SetDefaultMonospacedFont(PDF_FONT_MONOSPACED);

// set margins
$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);
$pdf->SetHeaderMargin(PDF_MARGIN_HEADER);
$pdf->SetFooterMargin(PDF_MARGIN_FOOTER);

// set auto page breaks
$pdf->SetAutoPageBreak(TRUE, PDF_MARGIN_BOTTOM);

// set image scale factor
$pdf->setImageScale(PDF_IMAGE_SCALE_RATIO);

// set some language-dependent strings (optional)
if (@file_exists(dirname(__FILE__).'/lang/eng.php')) {
	require_once(dirname(__FILE__).'/lang/eng.php');
	$pdf->setLanguageArray($l);
}

// ---------------------------------------------------------

// set font
$pdf->SetFont('helvetica', 'B', 20);

// add a page
$pdf->AddPage();

// set some text to print
$txt = <<<EOD
My PDF text
EOD;

// print a block of text using Write()
$pdf->Write(0, $txt, '', 0, 'C', true, 0, false, false, 0);

// ---------------------------------------------------------

//Close and output PDF document
$pdf->Output('example_001.pdf', 'I');
```

This code will create a PDF document with a footer. The footer will be set using the `setFooterData` method, and the font of the footer can be set using the `setFooterFont` method. The PDF is then outputted using the `Output` method.

The parts of the code used for adding a footer to a PDF document are:

- `SetHeaderData` - Sets the document header data
- `setFooterData` - Sets the document footer data
- `setHeaderFont` - Sets the font for the header
- `setFooterFont` - Sets the font for the footer
- `Output` - Outputs the PDF document

For more information about how to add a footer to a PDF generated with PHP and TCPDF, please refer to the [TCPDF documentation](https://tcpdf.org/examples/example_001/).

onelinerhub: [How can I add a footer to a PDF generated using PHP and TCPDF?](https://onelinerhub.com/php-tcpdf/how-can-i-add-a-footer-to-a-pdf-generated-using-php-and-tcpdf)