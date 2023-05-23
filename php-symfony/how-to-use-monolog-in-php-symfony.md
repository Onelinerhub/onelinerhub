# How to use Monolog in PHP Symfony?
// plain

Monolog is a logging library for PHP Symfony applications. It provides a simple and powerful way to log messages to various log handlers.

To use Monolog in a Symfony application, first install the MonologBundle package:

```
composer require symfony/monolog-bundle
```

Then, create a logger service in the `config/services.yaml` file:

```
# config/services.yaml
services:
    App\Logger\MyLogger:
        arguments: ['@monolog.logger.my_logger']
```

The code above creates a service called `App\Logger\MyLogger` that uses the `my_logger` logger from Monolog.

To use the logger, inject it into a controller or service:

```
// src/Controller/MyController.php

use App\Logger\MyLogger;

class MyController
{
    private $logger;

    public function __construct(MyLogger $logger)
    {
        $this->logger = $logger;
    }

    public function index()
    {
        $this->logger->info('This is a log message');
    }
}
```

The code above injects the `MyLogger` service into the `MyController` controller and uses it to log a message.

## Helpful links

- [MonologBundle Documentation](https://symfony.com/doc/current/bundles/MonologBundle/index.html)
- [Monolog Documentation](https://github.com/Seldaek/monolog)

onelinerhub: [How to use Monolog in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-monolog-in-php-symfony)