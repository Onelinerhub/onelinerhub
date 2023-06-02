# How can I use PHP and TCPDF together to generate a PDF in Java?
// plain

PHP and TCPDF can be used together to generate a PDF in Java. The following example code can be used to generate a PDF:
```
<?php
require_once('tcpdf_include.php');

// create new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Author');
$pdf->SetTitle('Title');
$pdf->SetSubject('Subject');
$pdf->SetKeywords('Keywords');

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

// set default font subsetting mode
$pdf->setFontSubsetting(true);

// set font
$pdf->SetFont('helvetica', '', 14, '', true);

// add a page
$pdf->AddPage();

// set text shadow effect
$pdf->setTextShadow(array('enabled'=>true, 'depth_w'=>0.2, 'depth_h'=>0.2, 'color'=>array(196,196,196), 'opacity'=>1, 'blend_mode'=>'Normal'));

// Set some content to print
$html = <<<EOD
<h1>TCPDF Example 001</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
<p>This is an example of <i>TCPDF</i> which generates PDF files in Java.</p>
EOD;

// Print text using writeHTMLCell()
$pdf->writeHTMLCell(0, 0, '', '', $html, 0, 1, 0, true, '', true);

// ---------------------------------------------------------

// Close and output PDF document
// This method has several options, check the source code documentation for more information.
$pdf->Output('example_001.pdf', 'I');
```

The above code will generate a PDF file with the following output:

<img src="example_001.png" alt="TCPDF Example 001 Output" width="400">

The code consists of the following parts:

1. `require_once('tcpdf_include.php');` - This includes the TCPDF library.
2. `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);` - This creates a new PDF document.
3. `$pdf->SetCreator(PDF_CREATOR);` - This sets the document creator.
4. `$pdf->SetHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING, array(0,64,255), array(0,64,128));` - This sets the header data for the document.
5. `$pdf->setFooterData(array(0,64,0), array(0,64,128));` - This sets the footer data for the document.
6. `$pdf->SetFont('helvetica', '', 14, '', true);` - This sets the font for the document.
7. `$pdf->writeHTMLCell(0, 0, '', '', $html, 0, 1, 0, true, '', true);` - This prints the HTML content in the document.
8. `$pdf->Output('example_001.pdf', 'I');` - This outputs the PDF document.

## Helpful links

- [TCPDF Documentation](https://tcpdf.org/docs.php)
- [TCPDF Examples](https://tcpdf.org/examples/)

onelinerhub: [How can I use PHP and TCPDF together to generate a PDF in Java?](https://onelinerhub.com/php-tcpdf/how-can-i-use-php-and-tcpdf-together-to-generate-a-pdf-in-java)