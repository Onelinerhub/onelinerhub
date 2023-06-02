# How do I set footer data using PHP TCPDF?
// plain

To set footer data using PHP TCPDF, first we need to create a new TCPDF instance by passing the page size, orientation and unit.

```
$pdf = new TCPDF('P', 'mm', 'A4', true, 'UTF-8', false);
```

Then we need to set the PDF's page margins.

```
$pdf->SetMargins(PDF_MARGIN_LEFT, PDF_MARGIN_TOP, PDF_MARGIN_RIGHT);
```

After that, we can set the header and footer by using the `setHeaderData()` and `setFooterData()` methods.

```
// set header data
$pdf->setHeaderData(PDF_HEADER_LOGO, PDF_HEADER_LOGO_WIDTH, PDF_HEADER_TITLE.' 001', PDF_HEADER_STRING);

// set footer data
$pdf->setFooterData(array(0,64,0), array(0,64,128));
```

The `setHeaderData()` and `setFooterData()` methods take two parameters. The first parameter is an array of RGB values for the background color. The second parameter is an array of RGB values for the text color.

Finally, we can set the font for the footer data.

```
$pdf->setFooterFont(Array(PDF_FONT_NAME_DATA, '', PDF_FONT_SIZE_DATA));
```

## Helpful links

- [TCPDF Documentation](https://tcpdf.org/docs/code/classTCPDF.html)
- [TCPDF Example](https://tcpdf.org/examples/example_001/)

onelinerhub: [How do I set footer data using PHP TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-set-footer-data-using-php-tcpdf)