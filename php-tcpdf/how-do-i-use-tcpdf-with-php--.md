# How do I use TCPDF with PHP 8?
// plain

Using TCPDF with PHP 8 is easy. To get started, you'll need to include the TCPDF library in your PHP file:
```php
require_once('tcpdf/tcpdf.php');
```

Next, you'll need to create an instance of the TCPDF class and set some global variables:
```php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('Author');
$pdf->SetTitle('Title');
$pdf->SetSubject('Subject');
$pdf->SetKeywords('keywords');
```

Once the instance is created, you can use the TCPDF library to generate PDF documents. For example, you can add a page to the PDF document like this:
```php
$pdf->AddPage();
```

You can also add content to the PDF document, like text, images, and HTML. Here's an example of adding text to the PDF document:
```php
$pdf->Write(0, 'Hello World!', '', 0, 'L', true, 0, false, false, 0);
```

Finally, you can output the PDF document to the browser or save it to a file:
```php
$pdf->Output('example.pdf', 'I');
```

That's all you need to do to use TCPDF with PHP 8. For more information, please see the [TCPDF documentation](https://tcpdf.org/docs/).

onelinerhub: [How do I use TCPDF with PHP 8?](https://onelinerhub.com/php-tcpdf/how-do-i-use-tcpdf-with-php--)