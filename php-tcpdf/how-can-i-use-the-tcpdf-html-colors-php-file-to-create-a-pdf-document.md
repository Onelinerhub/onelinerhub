# How can I use the tcpdf html colors.php file to create a PDF document?
// plain

To create a PDF document using the tcpdf html colors.php file, you can use the following example code:

```
<?php
require_once('tcpdf_include.php');

$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);

$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Author Name');
$pdf->SetTitle('Title of PDF Document');
$pdf->SetSubject('Subject of PDF Document');

require_once('htmlcolors.php');

$pdf->SetTextColorArray($htmlColorArray['darkred']);
$pdf->SetFont('helvetica', 'B', 16);
$pdf->Cell(0, 0, 'Hello World!', 0, 1, 'C', 0, '', 0);

$pdf->Output('example_001.pdf', 'I');
```

This code will output a PDF document with the text "Hello World!" in dark red color.

The code consists of the following parts:
1. Require the tcpdf_include.php file which contains the TCPDF class.
2. Create a new instance of the TCPDF class.
3. Set the creator, author, title and subject of the PDF document.
4. Require the htmlcolors.php file which contains the HTML color codes.
5. Set the text color to the dark red color from the htmlcolors.php file.
6. Set the font and font size of the text.
7. Use the Cell() method to add the text to the PDF document.
8. Output the PDF document.

## Helpful links
- [TCPDF Documentation](https://tcpdf.org/docs/srcdoc/tcpdf/)
- [htmlcolors.php File](https://github.com/tecnickcom/TCPDF/blob/master/include/htmlcolors.php)

onelinerhub: [How can I use the tcpdf html colors.php file to create a PDF document?](https://onelinerhub.com/php-tcpdf/how-can-i-use-the-tcpdf-html-colors-php-file-to-create-a-pdf-document)