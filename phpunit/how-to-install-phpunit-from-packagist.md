# How to install PHPUnit from Packagist?
// plain

1. Install [Composer](https://getcomposer.org/download/) if you don't have it already.
2. Create a `composer.json` file in the root of your project and add the following code:
```json
{
    "require-dev": {
        "phpunit/phpunit": "^8.5"
    }
}
```
3. Run `composer install` in the root of your project.
4. Add the following line to your `php.ini` file:
```
zend_extension=xdebug.so
```
5. Run `phpunit` in the root of your project to verify the installation.

You should see the following output:
```
PHPUnit 8.5.2 by Sebastian Bergmann and contributors.

Usage:
  phpunit [options] UnitTest [UnitTest.php]
  phpunit [options] <directory>

...
```

onelinerhub: [How to install PHPUnit from Packagist?](https://onelinerhub.com/phpunit/how-to-install-phpunit-from-packagist)