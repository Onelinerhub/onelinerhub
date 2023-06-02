# How do I use TCPDF with PHP?
// plain

TCPDF is a PHP class for generating PDF documents. It can be used easily with PHP to create and manipulate PDF documents.

To use TCPDF, the following steps should be taken:

1. Download the latest version of TCPDF from [https://tcpdf.org/](https://tcpdf.org/).

2. Unzip the file and move the "tcpdf.php" and "config" folder to the root directory of your project.

3. Include the "tcpdf.php" file in your project:

```php
require_once('tcpdf.php');
```

4. Create a new instance of the TCPDF class:

```php
$pdf = new TCPDF();
```

5. Generate the PDF document using the TCPDF methods:

```php
$pdf->AddPage();
$pdf->Write(0, 'Hello World!');
$pdf->Output('hello_world.pdf', 'D');
```

6. Output the PDF document:

```php
$pdf->Output('hello_world.pdf', 'D');
```

7. The PDF document will be downloaded to the user's computer.

For more information about TCPDF, please refer to the [TCPDF Documentation](https://tcpdf.org/docs/).

onelinerhub: [How do I use TCPDF with PHP?](https://onelinerhub.com/php-tcpdf/how-do-i-use-tcpdf-with-php-1685691033)