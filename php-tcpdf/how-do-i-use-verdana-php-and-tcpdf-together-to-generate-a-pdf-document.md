# How do I use Verdana.php and TCPDF together to generate a PDF document?
// plain

Verdana.php and TCPDF can be used together to generate a PDF document. To do this, first import Verdana.php and TCPDF into a project:
```
require_once('/path/to/verdana.php');
require_once('/path/to/tcpdf.php');
```

Next, create a new TCPDF instance and set the font to Verdana:
```
$pdf = new TCPDF();
$pdf->SetFont('Verdana');
```

Then, add content to the PDF using the `WriteHTML()` method:
```
$pdf->WriteHTML('<h1>Hello World</h1>');
```

Finally, output the PDF with the `Output()` method:
```
$pdf->Output('example.pdf', 'F');
```

## Code explanation

- `require_once('/path/to/verdana.php');` - imports the Verdana.php library
- `require_once('/path/to/tcpdf.php');` - imports the TCPDF library
- `$pdf = new TCPDF();` - creates a new TCPDF instance
- `$pdf->SetFont('Verdana');` - sets the font to Verdana
- `$pdf->WriteHTML('<h1>Hello World</h1>');` - adds content to the PDF
- `$pdf->Output('example.pdf', 'F');` - outputs the PDF

## Helpful links
- [Verdana.php](https://github.com/dompdf/dompdf/tree/master/lib/fonts/Verdana.php)
- [TCPDF](https://tcpdf.org/)

onelinerhub: [How do I use Verdana.php and TCPDF together to generate a PDF document?](https://onelinerhub.com/php-tcpdf/how-do-i-use-verdana-php-and-tcpdf-together-to-generate-a-pdf-document)