# How do I install TCPDF using Yum on a PHP server?
// plain

1. Install the EPEL repository on the server by running the command:
```
yum install epel-release
```
2. Install the TCPDF package using the command:
```
yum install php-tcpdf
```
3. Enable the TCPDF extension in the php.ini configuration file by adding the following line:
```
extension=tcpdf.so
```
4. Restart the PHP service on the server with the command:
```
systemctl restart php-fpm
```
5. Verify that the TCPDF extension is installed and enabled by running the command:
```
php -m | grep tcpdf
```
**Output**: `tcpdf`

6. To use TCPDF, include the library with the following code:
```php
require_once('/usr/share/php/tcpdf/tcpdf.php');
```
7. Create a new instance of the TCPDF class and use it to generate PDFs:
```php
$pdf = new TCPDF();
$pdf->AddPage();
$pdf->Write(0, 'Hello world!');
$pdf->Output('example.pdf', 'D');
```

## Code explanation
**

1. `yum install epel-release` - This command installs the EPEL repository on the server.
2. `yum install php-tcpdf` - This command installs the TCPDF package.
3. `extension=tcpdf.so` - This line enables the TCPDF extension in the php.ini configuration file.
4. `systemctl restart php-fpm` - This command restarts the PHP service on the server.
5. `php -m | grep tcpdf` - This command verifies that the TCPDF extension is installed and enabled.
6. `require_once('/usr/share/php/tcpdf/tcpdf.php');` - This code includes the TCPDF library.
7. `$pdf = new TCPDF();` - This creates a new instance of the TCPDF class.

**## Helpful links**

- [TCPDF Documentation](https://tcpdf.org/docs.php)
- [How to Install EPEL Repository on CentOS 8](https://www.tecmint.com/install-epel-repository-on-centos/)

onelinerhub: [How do I install TCPDF using Yum on a PHP server?](https://onelinerhub.com/php-tcpdf/how-do-i-install-tcpdf-using-yum-on-a-php-server)