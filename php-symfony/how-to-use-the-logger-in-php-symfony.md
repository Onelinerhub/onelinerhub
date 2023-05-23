# How to use the logger in PHP Symfony?
// plain

Using the logger in PHP Symfony is easy and straightforward.

```
// Get the logger service
$logger = $this->get('logger');

// Log a message
$logger->info('This is an info message');
```

The code above will log an info message.

## Code explanation


1. `$logger = $this->get('logger');` - This line gets the logger service.
2. `$logger->info('This is an info message');` - This line logs an info message.

## Helpful links

- [Logging in Symfony](https://symfony.com/doc/current/logging.html)
- [Monolog Documentation](https://symfony.com/doc/current/components/logger.html)

onelinerhub: [How to use the logger in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-the-logger-in-php-symfony)