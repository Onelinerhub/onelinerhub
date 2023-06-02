# How can I use PHP and XPath to generate PDFs with TCPDF?
// plain

Using PHP and XPath to generate PDFs with TCPDF is possible by utilizing TCPDF's ability to parse HTML and the PHP DOMDocument class to parse XML.

To begin, you'll need to create a new instance of the TCPDF class and set the page size, margins, and orientation.

```php
// create new PDF document
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Your Name');
$pdf->SetTitle('Your Title');
$pdf->SetSubject('Your Subject');
$pdf->SetKeywords('Your Keywords');

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
```

Once the PDF is setup, you can use the PHP DOMDocument class to parse an XML file and use XPath to query it for the data you need. Then, you can use the TCPDF's writeHTML() method to write the data to the PDF.

```php
// Load XML
$xml = new DOMDocument();
$xml->load('data.xml');

// Get data using XPath
$xpath = new DOMXPath($xml);
$items = $xpath->query('//item');

// Generate HTML
$html = '';
foreach ($items as $item) {
    $html .= '<h1>' . $item->getAttribute('name') . '</h1>';
    $html .= '<p>' . $item->nodeValue . '</p>';
}

// Write data to PDF
$pdf->AddPage();
$pdf->writeHTML($html, true, false, true, false, '');
```

Finally, you can call the TCPDF's Output() method to save the PDF to a file or stream it to the user's browser.

```php
$pdf->Output('example.pdf', 'I');
```

#### Code Parts Explanation

* `$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);` - Create a new instance of the TCPDF class and set the page size, margins, and orientation.
* `$pdf->SetCreator(PDF_CREATOR);` - Set document information.
* `$xml = new DOMDocument();` - Create a new DOMDocument object.
* `$xml->load('data.xml');` - Load the XML file.
* `$xpath = new DOMXPath($xml);` - Create a new DOMXPath object.
* `$items = $xpath->query('//item');` - Query the XML for the data needed.
* `$html .= '<h1>' . $item->getAttribute('name') . '</h1>';` - Generate HTML from the queried data.
* `$pdf->AddPage();` - Add a new page to the PDF.
* `$pdf->writeHTML($html, true, false, true, false, '');` - Write the HTML to the PDF.
* `$pdf->Output('example.pdf', 'I');` - Output the PDF to a file or stream it to the user's browser.

#### Relevant Links

* [TCPDF Documentation](https://tcpdf.org/docs/getting-started/)
* [PHP DOMDocument Class](https://www.php.net/manual/en/class.domdocument.php)
* [PHP DOMXPath Class](https://www.php.net/manual/en/class.domxpath.php)

onelinerhub: [How can I use PHP and XPath to generate PDFs with TCPDF?](https://onelinerhub.com/php-tcpdf/how-can-i-use-php-and-xpath-to-generate-pdfs-with-tcpdf)