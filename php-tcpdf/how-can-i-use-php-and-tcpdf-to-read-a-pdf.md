# How can I use PHP and TCPDF to read a PDF?
// plain

Using PHP and TCPDF, you can read a PDF by using the `TCPDF::setSourceFile()` method. This method takes the path to the PDF file as its parameter and sets it as the source file for the `TCPDF` object.

```
$pdf = new TCPDF();
$pdf->setSourceFile("my_pdf.pdf");
```

You can then use the `TCPDF::importPage()` method to import a single page from the source PDF file. This method takes two parameters: the page number and the desired page size.

```
$page_number = 1;
$page_size = array(210, 297); // A4 size
$pdf->importPage($page_number, $page_size);
```

You can also use the `TCPDF::getNumPages()` method to get the total number of pages in the source PDF file.

```
$total_pages = $pdf->getNumPages();
```

Finally, you can use the `TCPDF::Output()` method to output the PDF file.

```
$pdf->Output('my_pdf.pdf', 'I');
```

The `TCPDF` class also provides several other methods for reading and manipulating PDF files, such as `TCPDF::SetFont()`, `TCPDF::SetXY()`, `TCPDF::Write()`, etc.

## Helpful links

- [TCPDF Documentation](https://tcpdf.org/docs/index.php)
- [PHP TCPDF Examples](https://www.php-fig.org/tcpdf/examples/)

onelinerhub: [How can I use PHP and TCPDF to read a PDF?](https://onelinerhub.com/php-tcpdf/how-can-i-use-php-and-tcpdf-to-read-a-pdf)