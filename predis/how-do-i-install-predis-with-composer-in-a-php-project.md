# How do I install Predis with Composer in a PHP project?
// plain

1. Add the Predis package to the `require` section of your `composer.json` file:
```json
{
    "require": {
        "predis/predis": "^1.1"
    }
}
```

2. Run `composer install` in the project directory to install Predis.

3. After installation, require the autoloader in your PHP code:
```php
require 'vendor/autoload.php';
```

4. Create a new instance of the `Predis\Client` class:
```php
$client = new Predis\Client();
```

5. Use the `$client` object to connect to Redis, execute commands, and interact with the data store.

6. For more information, see the [Predis documentation](https://github.com/nrk/predis).

7. For more information about Composer, see the [Composer documentation](https://getcomposer.org/doc/).

onelinerhub: [How do I install Predis with Composer in a PHP project?](https://onelinerhub.com/predis/how-do-i-install-predis-with-composer-in-a-php-project)