# How to set the log level in PHP Symfony?
// plain

The log level in PHP Symfony can be set by using the `logger` service.

```
$logger = $this->get('logger');
$logger->setLevel(Logger::ERROR);
```

The above code sets the log level to `ERROR`.

The following are the available log levels in PHP Symfony:

- `Logger::EMERGENCY`: System is unusable
- `Logger::ALERT`: Action must be taken immediately
- `Logger::CRITICAL`: Critical conditions
- `Logger::ERROR`: Error conditions
- `Logger::WARNING`: Warning conditions
- `Logger::NOTICE`: Normal but significant condition
- `Logger::INFO`: Informational messages
- `Logger::DEBUG`: Debug-level messages

## Helpful links

- [Logging in Symfony](https://symfony.com/doc/current/logging.html)
- [Monolog Documentation](https://symfony.com/doc/current/components/monolog.html)

onelinerhub: [How to set the log level in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-set-the-log-level-in-php-symfony)