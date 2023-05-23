# How to use Bundles with PHP Symfony?
// plain

Bundles are the main building blocks of a Symfony application. They are like plugins that can be installed and used to extend the functionality of the application.

To use a bundle, you first need to install it using Composer. Then, you need to enable it in the `config/bundles.php` file.

```php
<?php

return [
    // ...
    App\SomeBundle\SomeBundle::class => ['all' => true],
    // ...
];
```

Once enabled, you can use the bundle's services, routes, and other features.

- Installing a bundle: Use Composer to install the bundle.
- Enabling a bundle: Add the bundle class to the `config/bundles.php` file.
- Using a bundle: Use the bundle's services, routes, and other features.

## Helpful links
- [Symfony Bundles Documentation](https://symfony.com/doc/current/bundles.html)
- [Composer Documentation](https://getcomposer.org/doc/)

onelinerhub: [How to use Bundles with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-bundles-with-php-symfony)