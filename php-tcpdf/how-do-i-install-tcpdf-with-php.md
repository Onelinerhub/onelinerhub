# How do I install TCPDF with PHP?
// plain

To install TCPDF with PHP, follow these steps:

1. Download the [TCPDF library](http://www.tcpdf.org/download.php) and extract the files to a directory.

2. Include the TCPDF library in your PHP script using the `require_once` command.

```php
require_once('path/to/tcpdf_include.php');
```

3. Create a new TCPDF object, passing the page size, page orientation, and language settings as parameters.

```php
$pdf = new TCPDF('P', 'mm', 'A4', true, 'UTF-8', false);
```

4. Set the document information and creator (optional).

```php
$pdf->SetCreator('My Creator');
$pdf->SetTitle('My Title');
```

5. Add the content you wish to include in your PDF.

```php
$pdf->Write(0, 'My Content', '', 0, 'L', true, 0, false, false, 0);
```

6. Output the PDF file using the `Output` method.

```php
$pdf->Output('myfile.pdf', 'I');
```

7. Finally, delete the TCPDF object to free up memory.

```php
unset($pdf);
```

onelinerhub: [How do I install TCPDF with PHP?](https://onelinerhub.com/php-tcpdf/how-do-i-install-tcpdf-with-php)