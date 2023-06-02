# How do I install and configure Remi's PHP-TCPDF on a web server?
// plain

1. Download the latest version of [PHP-TCPDF](https://sourceforge.net/projects/tcpdf/files/latest/download) from Sourceforge.
2. Extract the files to the web server and move the extracted files to the desired location.
3. Create a configuration file for PHP-TCPDF and save it as `tcpdf_config.php` in the same directory as the extracted files.

```php
<?php
define ('K_TCPDF_EXTERNAL_CONFIG', true);
define ('K_PATH_MAIN', '/path/to/tcpdf/');
define ('K_PATH_URL', 'http://www.example.com/tcpdf/');
define ('K_PATH_FONTS', K_PATH_MAIN.'fonts/');
define ('K_PATH_CACHE', K_PATH_MAIN.'cache/');
define ('K_PATH_URL_CACHE', K_PATH_URL.'cache/');
define ('K_PATH_IMAGES', K_PATH_MAIN.'images/');
define ('K_BLANK_IMAGE', K_PATH_IMAGES.'_blank.png');
define ('PDF_PAGE_FORMAT', 'A4');
define ('PDF_PAGE_ORIENTATION', 'P');
define ('PDF_CREATOR', 'TCPDF');
define ('PDF_AUTHOR', 'TCPDF');
define ('PDF_HEADER_TITLE', 'TCPDF Example');
define ('PDF_HEADER_STRING', "by Remi \xD7\xA9");
define ('PDF_UNIT', 'mm');
define ('PDF_MARGIN_HEADER', 5);
define ('PDF_MARGIN_FOOTER', 10);
define ('PDF_MARGIN_TOP', 27);
define ('PDF_MARGIN_BOTTOM', 25);
define ('PDF_MARGIN_LEFT', 15);
define ('PDF_MARGIN_RIGHT', 15);
define ('PDF_FONT_NAME_MAIN', 'helvetica');
define ('PDF_FONT_SIZE_MAIN', 10);
define ('PDF_FONT_NAME_DATA', 'helvetica');
define ('PDF_FONT_SIZE_DATA', 8);
define ('PDF_FONT_MONOSPACED', 'courier');
define ('PDF_IMAGE_SCALE_RATIO', 1.25);
define ('HEAD_MAGNIFICATION', 1.1);
define('K_CELL_HEIGHT_RATIO', 1.25);
define('K_TITLE_MAGNIFICATION', 1.3);
define('K_SMALL_RATIO', 2/3);
?>
```

4. Create a PHP file that will generate the PDF document and save it as `tcpdf_example.php` in the same directory as the extracted files.

```php
<?php
require_once('tcpdf_config.php');
require_once('tcpdf.php');

// create new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Remi');
$pdf->SetTitle('TCPDF Example');
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
<h1>Welcome to TCPDF!</h1>
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
$pdf->Output('example_001.pdf', 'I');

//============================================================+
// END OF FILE
//============================================================+
```

5. Open a web browser and access the `tcpdf_example.php` file to generate the PDF document.
6. The PDF document should now be generated and displayed in the web browser.
7. For more information, check out the [PHP-TCPDF documentation](https://tcpdf.org/docs/user-guide/).

onelinerhub: [How do I install and configure Remi's PHP-TCPDF on a web server?](https://onelinerhub.com/php-tcpdf/how-do-i-install-and-configure-remi-s-php-tcpdf-on-a-web-server)