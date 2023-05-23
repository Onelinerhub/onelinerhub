# How to access the log in PHP Symfony?
// plain

To access the log in PHP Symfony, you can use the `getLogger()` method of the `Logger` class. This method returns an instance of the `Logger` class, which can be used to log messages.

## Example code

```php
$logger = new Logger();
$logger->getLogger()->info('This is an info message');
```

## Output example

```
[2020-04-20 10:00:00] app.INFO: This is an info message [] []
```

The code above creates an instance of the `Logger` class and then calls the `getLogger()` method to get an instance of the `Logger` class. The `info()` method is then used to log an info message.

The `Logger` class also provides other methods for logging messages, such as `debug()`, `warning()`, `error()`, and `critical()`.

## Helpful links

- [Logging in Symfony](https://symfony.com/doc/current/logging.html)
- [Logger Class](https://api.symfony.com/4.4/Symfony/Component/HttpKernel/Log/Logger.html)

onelinerhub: [How to access the log in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-access-the-log-in-php-symfony)