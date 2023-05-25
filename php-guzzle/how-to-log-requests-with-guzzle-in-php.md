# How to log requests with Guzzle in PHP?
// plain

Logging requests with Guzzle in PHP is easy and straightforward. To enable logging, you need to create a logger object and pass it to the Guzzle client.

```php
$logger = new \Monolog\Logger('guzzle');
$logger->pushHandler(new \Monolog\Handler\StreamHandler('guzzle.log'));

$client = new \GuzzleHttp\Client([
    'handler' => \GuzzleHttp\HandlerStack::create(),
    'logger' => $logger
]);
```

The above code will create a logger object and pass it to the Guzzle client. The logger will write the log messages to the `guzzle.log` file.

## Code explanation


1. `$logger = new \Monolog\Logger('guzzle');` - creates a logger object.
2. `$logger->pushHandler(new \Monolog\Handler\StreamHandler('guzzle.log'));` - adds a handler to the logger object which will write the log messages to the `guzzle.log` file.
3. `$client = new \GuzzleHttp\Client([` - creates a Guzzle client.
4. `'handler' => \GuzzleHttp\HandlerStack::create(),` - creates a handler stack.
5. `'logger' => $logger` - adds the logger object to the Guzzle client.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Monolog Documentation](https://github.com/Seldaek/monolog)

onelinerhub: [How to log requests with Guzzle in PHP?](https://onelinerhub.com/php-guzzle/how-to-log-requests-with-guzzle-in-php)