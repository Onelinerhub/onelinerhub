# How to install MySQL extension for PHP?
// plain

1. To install MySQL extension for PHP, you need to have the MySQL server installed and running.
2. Then, you need to install the PHP MySQL extension. This can be done by running the following command in the terminal:
```
$ sudo apt-get install php-mysql
```
3. After the installation is complete, you need to restart the web server for the changes to take effect.
4. You can then verify that the MySQL extension is installed by running the following command in the terminal:
```
$ php -m | grep mysql
```
5. The output should be something like this:
```
mysql
mysqli
pdo_mysql
```

## Helpful links

- [MySQL Installation Guide](https://dev.mysql.com/doc/refman/8.0/en/installing.html)
- [PHP MySQL Extension Installation Guide](https://www.php.net/manual/en/mysql.installation.php)

onelinerhub: [How to install MySQL extension for PHP?](https://onelinerhub.com/php-mysql/how-to-install-mysql-extension-for-php)