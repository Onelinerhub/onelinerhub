# How to install PCNTL for PHP using Brew?
// plain

Installing PCNTL for PHP using Brew is a simple process.

1. First, open the terminal and run the following command:
```
brew install php71-pcntl
```
2. This will install the PCNTL extension for PHP 7.1.

3. After the installation is complete, you need to enable the extension in your php.ini file. To do this, open the php.ini file and add the following line:
```
extension=pcntl.so
```
4. Finally, restart your web server to apply the changes.

5. You can now use the PCNTL functions in your PHP code.

## Code explanation


1. `brew install php71-pcntl` - This command installs the PCNTL extension for PHP 7.1.

2. `extension=pcntl.so` - This line enables the PCNTL extension in the php.ini file.

3. `restart your web server` - This command restarts the web server to apply the changes.

## Helpful links

- [PHP PCNTL Documentation](https://www.php.net/manual/en/book.pcntl.php)

onelinerhub: [How to install PCNTL for PHP using Brew?](https://onelinerhub.com/php-pcntl/how-to-install-pcntl-for-php-using-brew)