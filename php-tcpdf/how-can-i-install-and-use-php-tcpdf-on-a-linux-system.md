# How can I install and use PHP-TCPDF on a Linux system?
// plain

1. Download the PHP-TCPDF library from the official website: [https://tcpdf.org/](https://tcpdf.org/).
2. Unzip the library to a folder of your choice.
3. Include the library in your PHP script:
```php
require_once('/path/to/tcpdf.php');
```
4. Create a new TCPDF instance:
```php
$pdf = new TCPDF();
```
5. Use the available methods to create your PDF document:
```php
$pdf->AddPage();
$pdf->Write(0, 'Hello World!');
$pdf->Output('example.pdf', 'I');
```
6. The output of the code above will be a PDF file with the content `Hello World!`.
7. Refer to the [official documentation](https://tcpdf.org/docs.php) for more information.

onelinerhub: [How can I install and use PHP-TCPDF on a Linux system?](https://onelinerhub.com/php-tcpdf/how-can-i-install-and-use-php-tcpdf-on-a-linux-system)