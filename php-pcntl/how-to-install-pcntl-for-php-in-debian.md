# How to install PCNTL for PHP in Debian?
// plain

1. PCNTL is a PHP extension that provides process control support for Unix-like operating systems.
2. To install PCNTL for PHP in Debian, first install the `php-dev` package:
```
sudo apt-get install php-dev
```
3. Then, install the `libpcre3-dev` package:
```
sudo apt-get install libpcre3-dev
```
4. Finally, install the `php-pear` package:
```
sudo apt-get install php-pear
```
5. After that, you can install PCNTL for PHP using the `pecl` command:
```
sudo pecl install pcntl
```

## Code explanation


1. `sudo apt-get install php-dev`: This command installs the `php-dev` package, which is required for building PHP extensions.
2. `sudo apt-get install libpcre3-dev`: This command installs the `libpcre3-dev` package, which is required for building PCNTL.
3. `sudo apt-get install php-pear`: This command installs the `php-pear` package, which is required for installing PHP extensions using the `pecl` command.
4. `sudo pecl install pcntl`: This command installs PCNTL for PHP.

## Helpful links

- [PHP PCNTL Documentation](https://www.php.net/manual/en/book.pcntl.php)
- [How To Install PHP PECL Extensions on Debian 10](https://www.digitalocean.com/community/tutorials/how-to-install-php-pecl-extensions-on-debian-10)

onelinerhub: [How to install PCNTL for PHP in Debian?](https://onelinerhub.com/php-pcntl/how-to-install-pcntl-for-php-in-debian)