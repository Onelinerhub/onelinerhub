# How to install the PHP MySQL extension on Ubuntu?
// plain

1. Install the `php-mysql` package using apt:
```
sudo apt-get install php-mysql
```
2. Enable the extension in the `php.ini` configuration file:
```
extension=mysql.so
```
3. Restart the web server to apply the changes:
```
sudo service apache2 restart
```
4. Verify the installation by creating a `phpinfo.php` file:
```
<?php
phpinfo();
?>
```
5. Access the file in a web browser and check for the `mysql` section in the output:
```
mysql
MySQL Support => enabled
Client API version => 5.7.25
```

## Helpful links
- [PHP MySQL Extension](https://www.php.net/manual/en/book.mysql.php)
- [Ubuntu Packages](https://packages.ubuntu.com/search?keywords=php-mysql)

onelinerhub: [How to install the PHP MySQL extension on Ubuntu?](https://onelinerhub.com/php-mysql/how-to-install-the-php-mysql-extension-on-ubuntu)