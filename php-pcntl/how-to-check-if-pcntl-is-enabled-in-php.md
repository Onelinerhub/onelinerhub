# How to check if PCNTL is enabled in PHP?
// plain

To check if PCNTL is enabled in PHP, you can use the `phpinfo()` function. This will output information about the current PHP installation, including whether PCNTL is enabled.

```php
<?php
phpinfo();
```

## Output example

```
...
pcntl

PCNTL Support => enabled
...
```

Alternatively, you can use the `php -m` command to list all the modules that are enabled in the current PHP installation. If PCNTL is enabled, it will be listed in the output.

```
$ php -m
[PHP Modules]
...
pcntl
...
```

## Helpful links
- [PHP: pcntl - Manual](https://www.php.net/manual/en/book.pcntl.php)
- [How to check if a PHP extension is enabled?](https://stackoverflow.com/questions/1807907/how-to-check-if-a-php-extension-is-enabled)

onelinerhub: [How to check if PCNTL is enabled in PHP?](https://onelinerhub.com/php-pcntl/how-to-check-if-pcntl-is-enabled-in-php)