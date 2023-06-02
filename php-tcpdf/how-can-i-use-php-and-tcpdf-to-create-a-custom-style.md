# How can I use PHP and TCPDF to create a custom style?
// plain

PHP and TCPDF can be used to create a custom style by using the writeHTMLCell() method. This method allows you to specify the style of the text, such as font type, font size, font color, and background color. To create a custom style, the following code can be used:

```
<?php
// Include the TCPDF library
require_once('tcpdf_include.php');

// create new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Author Name');
$pdf->SetTitle('My Custom Style');
$pdf->SetSubject('TCPDF Tutorial');
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
$txt = 'My Custom Style';

// set style for barcode
$style = array(
	'border' => 2,
	'vpadding' => 'auto',
	'hpadding' => 'auto',
	'fgcolor' => array(0,0,0),
	'bgcolor' => false, //array(255,255,255)
	'module_width' => 1, // width of a single module in points
	'module_height' => 1 // height of a single module in points
);

// print a message
$pdf->writeHTMLCell(0, 0, '', '', $txt, 0, 1, 0, true, 'C', true);

// ---------------------------------------------------------

//Close and output PDF document
$pdf->Output('example_001.pdf', 'I');

//============================================================+
// END OF FILE
//============================================================+
```

The code above will create a PDF with the text "My Custom Style" using a custom style. The style can be customized by changing the parameters of the $style array. The parameters are:

* `border` - The width of the border, in points
* `vpadding` - The vertical padding, in points
* `hpadding` - The horizontal padding, in points
* `fgcolor` - The foreground color, as an array of RGB values
* `bgcolor` - The background color, as an array of RGB values
* `module_width` - The width of a single module, in points
* `module_height` - The height of a single module, in points

For more information, see the [TCPDF Documentation](https://tcpdf.org/docs/code/classTCPDF.html#ac7b1e3b5f8c0f9d3f62f0e7f6f5dd6d) and [WriteHTML() Method](https://tcpdf.org/docs/code/classTCPDF.html#acf0a7f5d6d9e8f7d7d9e8f7d7d9e8f7b).

onelinerhub: [How can I use PHP and TCPDF to create a custom style?](https://onelinerhub.com/php-tcpdf/how-can-i-use-php-and-tcpdf-to-create-a-custom-style)