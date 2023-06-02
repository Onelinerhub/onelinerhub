# How do I use PHP and TCPDF to create a project in Xcode?
// plain

Using PHP and TCPDF to create a project in Xcode is quite simple. First, download the TCPDF library from sourceforge.net. Then, create a new project in Xcode and make sure to include the TCPDF library in the project.

Next, create a file called “my_pdf.php” and add the following code to it:

```
<?php
require_once('tcpdf_include.php');

// create new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('My Author');
$pdf->SetTitle('My Title');
$pdf->SetSubject('My Subject');
$pdf->SetKeywords('My, Keywords');

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
<h1>My Title</h1>
<i>My Example</i>
<p>This is my example PDF document using TCPDF.</p>
EOD;

// Print text using writeHTMLCell()
$pdf->writeHTMLCell(0, 0, '', '', $html, 0, 1, 0, true, '', true);

// ---------------------------------------------------------

// Close and output PDF document
// This method has several options, check the source code documentation for more information.
$pdf->Output('example_001.pdf', 'I');

//============================================================+
// END OF FILE
//============================================================+
```

This code will create a PDF document with the title “My Title”, and it will include the text “My Example” and “This is my example PDF document using TCPDF.”

The code consists of the following parts:
* Lines 1-13: Require the TCPDF library and set the document information.
* Lines 15-25: Set the header and footer fonts, default monospaced font, margins, and auto page breaks.
* Lines 27-36: Set the default font subsetting mode and font.
* Lines 38-44: Add a page and set the text shadow effect.
* Lines 46-54: Set some content to print.
* Lines 56-64: Print the text using writeHTMLCell() and output the PDF document.

## Helpful links
* [TCPDF Sourceforge Page](https://sourceforge.net/projects/tcpdf/)
* [TCPDF Documentation](https://tcpdf.org/docs.php)

onelinerhub: [How do I use PHP and TCPDF to create a project in Xcode?](https://onelinerhub.com/php-tcpdf/how-do-i-use-php-and-tcpdf-to-create-a-project-in-xcode)