# How do I install TCPDF with Composer in a PHP project?
// plain

1. Install [Composer](https://getcomposer.org/) if it is not already installed.
2. Create a `composer.json` file in the root directory of the project and add the following code:
```json
{
    "require": {
        "tecnickcom/tcpdf": "^6.2"
    }
}
```
3. Run the command `composer install` in the project root directory.
4. This will install the TCPDF library in the `vendor` directory of the project.
5. Include the autoloader in the project by adding the following line at the top of the PHP file:
```php
require_once 'vendor/autoload.php';
```
6. To use the library, use the `use` keyword to import the namespace:
```php
use \TCPDF;
```
7. Create a new instance of the TCPDF class and use it to generate PDF documents:
```php
$pdf = new TCPDF();
```

## Helpful links
- https://getcomposer.org/
- https://packagist.org/packages/tecnickcom/tcpdf

onelinerhub: [How do I install TCPDF with Composer in a PHP project?](https://onelinerhub.com/php-tcpdf/how-do-i-install-tcpdf-with-composer-in-a-php-project)