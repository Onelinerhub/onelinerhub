# How do I use TCPDF with PHP 7.4?
// plain

To use TCPDF with PHP 7.4, first install the TCPDF library.

```
composer require tecnickcom/tcpdf
```

Then, include the library in the PHP script.

```
require_once('vendor/tecnick.com/tcpdf/tcpdf.php');
```

Next, create a new instance of the TCPDF class.

```
$pdf = new TCPDF();
```

Then, set the document information.

```
$pdf->SetTitle('My PDF Document');
$pdf->SetAuthor('John Doe');
$pdf->SetSubject('My PDF Document');
```

Next, add the content to the document.

```
$pdf->AddPage();
$pdf->Write(0, 'Hello World!');
```

Finally, output the document.

```
$pdf->Output('my_document.pdf', 'I');
```

## List of Code Parts

1. Install the TCPDF library: `composer require tecnickcom/tcpdf`
2. Include the library in the PHP script: `require_once('vendor/tecnick.com/tcpdf/tcpdf.php');`
3. Create a new instance of the TCPDF class: `$pdf = new TCPDF();`
4. Set the document information: `$pdf->SetTitle('My PDF Document');`
5. Add the content to the document: `$pdf->AddPage();`
6. Output the document: `$pdf->Output('my_document.pdf', 'I');`

## Relevant Links

- [TCPDF Library](https://tcpdf.org/)

onelinerhub: [How do I use TCPDF with PHP 7.4?](https://onelinerhub.com/php-tcpdf/how-do-i-use-tcpdf-with-php----)