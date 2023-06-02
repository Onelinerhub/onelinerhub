# How do I install php-tcpdf on CentOS 7?
// plain

1. Install EPEL repository:
```
sudo yum install epel-release
```
2. Install PHP-TCPDF package:
```
sudo yum install php-tcpdf
```
3. Verify the installation by checking the version of the installed package:
```
php -m | grep tcpdf
```
The output should be something like:
```
tcpdf
```
4. To use the TCPDF library in your PHP code, include the following line:
```
require_once('/usr/share/php/tcpdf/tcpdf.php');
```
5. To create a PDF file, create a new instance of the TCPDF class:
```
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```
6. To generate the PDF file, call the `Output` method:
```
$pdf->Output('example.pdf', 'I');
```
7. To learn more about the TCPDF library, please refer to the official [documentation](https://tcpdf.org/docs/).

onelinerhub: [How do I install php-tcpdf on CentOS 7?](https://onelinerhub.com/php-tcpdf/how-do-i-install-php-tcpdf-on-centos--)