# How can I use the PHP version of TCPDF?
// plain

The PHP version of TCPDF can be used to create PDF documents from within a PHP script. To use TCPDF, you must include the TCPDF library file in your PHP script. An example of how to include the library is shown below:

```
require_once('tcpdf/tcpdf.php');
```

Once the library is included, you can create a new instance of the TCPDF class and start adding content to the PDF document. For example, the following code will create a simple PDF document with a title and some text:

```
$pdf = new TCPDF();
$pdf->AddPage();
$pdf->SetTitle('My PDF Document');
$pdf->Write(0, 'My PDF Document Content');
$pdf->Output('myfile.pdf', 'I');
```

The code above will create a PDF document with the title 'My PDF Document' and the content 'My PDF Document Content'. The `Output` method will output the generated PDF to the browser or save it to a file.

In addition to creating PDF documents, TCPDF also provides a wide range of methods for manipulating PDF documents. For example, you can add images, tables, and other content to an existing PDF document.

To learn more about using TCPDF, please refer to the [official documentation](https://tcpdf.org/docs/).

onelinerhub: [How can I use the PHP version of TCPDF?](https://onelinerhub.com/php-tcpdf/how-can-i-use-the-php-version-of-tcpdf)