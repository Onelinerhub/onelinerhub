# How do I save a file using PHP and TCPDF?
// plain

To save a file using PHP and TCPDF, you can use the following code:
```
<?php

require_once('tcpdf/tcpdf.php');

// create new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Author Name');
$pdf->SetTitle('Document Title');
$pdf->SetSubject('Document Subject');
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

// set default font subsetting mode
$pdf->setFontSubsetting(true);

// Set font
// dejavusans is a UTF-8 Unicode font, if you only need to
// print standard ASCII chars, you can use core fonts like
// helvetica or times to reduce file size.
$pdf->SetFont('dejavusans', '', 14, '', true);

// Add a page
// This method has several options, check the source code documentation for more information.
$pdf->AddPage();

// set text shadow effect
$pdf->setTextShadow(array('enabled'=>true, 'depth_w'=>0.2, 'depth_h'=>0.2, 'color'=>array(196,196,196), 'opacity'=>1, 'blend_mode'=>'Normal'));

// Set some content to print
$html = <<<EOD
<h1>Welcome to <a href="http://www.tcpdf.org" style="text-decoration:none;background-color:#CC0000;color:black;">&nbsp;<span style="color:black;">TC</span><span style="color:white;">PDF</span>&nbsp;</a>!</h1>
<i>This is the first example of TCPDF library.</i>
<p>This text is printed using the <i>writeHTMLCell()</i> method but you can also use: <i>Multicell(), writeHTML(), Write(), Cell() and Text()</i>.</p>
<p>Please check the source code documentation and other examples for further information.</p>
<p style="color:#CC0000;">TO IMPROVE AND EXPAND TCPDF I NEED YOUR SUPPORT, PLEASE <a href="http://sourceforge.net/donate/index.php?group_id=128076">MAKE A DONATION!</a></p>
EOD;

// Print text using writeHTMLCell()
$pdf->writeHTMLCell(0, 0, '', '', $html, 0, 1, 0, true, '', true);

// ---------------------------------------------------------

// Close and output PDF document
// This method has several options, check the source code documentation for more information.
$pdf->Output('example_001.pdf', 'F');

//============================================================+
// END OF FILE
//============================================================+
```
This code will create a PDF file with the given HTML content and save it to the file `example_001.pdf`.

The code consists of the following parts:
1. Require the TCPDF library (`require_once('tcpdf/tcpdf.php');`)
2. Create a new TCPDF instance (`$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);`)
3. Set document information (`$pdf->SetCreator(PDF_CREATOR);`, `$pdf->SetAuthor('Author Name');`, `$pdf->SetTitle('Document Title');`, `$pdf->SetSubject('Document Subject');`, `$pdf->SetKeywords('TCPDF, PDF, example, test, guide');`)
4. Set header and footer data (`$pdf->SetHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING, array(0,64,255), array(0,64,128));`, `$pdf->setFooterData(array(0,64,0), array(0,64,128));`)
5. Set header and footer fonts (`$pdf->setHeaderFont(Array(PDF_FONT_NAME_MAIN, '', PDF_FONT_SIZE_MAIN));`, `$pdf->setFooterFont(Array(PDF_FONT_NAME_DATA, '', PDF_FONT_SIZE_DATA));`)
6. Set default monospaced font (`$pdf->SetDefaultMonospacedFont(PDF_FONT_MONOSPACED);`)
7. Set margins (`$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);`, `$pdf->SetHeaderMargin(PDF_MARGIN_HEADER);`, `$pdf->SetFooterMargin(PDF_MARGIN_FOOTER);`)
8. Set auto page breaks (`$pdf->SetAutoPageBreak(TRUE, PDF_MARGIN_BOTTOM);`)
9. Set image scale factor (`$pdf->setImageScale(PDF_IMAGE_SCALE_RATIO);`)
10. Set language-dependent strings (optional) (`if (@file_exists(dirname(__FILE__).'/lang/eng.php')) { require_once(dirname(__FILE__).'/lang/eng.php'); $pdf->setLanguageArray($l); }`)
11. Set default font subsetting mode (`$pdf->setFontSubsetting(true);`)
12. Set font (`$pdf->SetFont('dejavusans', '', 14, '', true);`)
13. Add a page (`$pdf->AddPage();`)
14. Set text shadow effect (`$pdf->setTextShadow(array('enabled'=>true, 'depth_w'=>0.2, 'depth_h'=>0.2, 'color'=>array(196,196,196), 'opacity'=>1, 'blend_mode'=>'Normal'));`)
15. Set some content to print (`$html = <<<EOD ... EOD;`)
16. Print text using writeHTMLCell() (`$pdf->writeHTMLCell(0, 0, '', '', $html, 0, 1, 0, true, '', true);`)
17. Output PDF document (`$pdf->Output('example_001.pdf', 'F');`)

For more information, please refer to the [TCPDF Documentation](https://tcpdf.org/docs/).

onelinerhub: [How do I save a file using PHP and TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-save-a-file-using-php-and-tcpdf)