# How to use Monolog with Guzzle in PHP?
// plain

Monolog is a logging library for PHP which can be used with Guzzle to log requests and responses.

```
use Monolog\Logger;
use Monolog\Handler\StreamHandler;

$logger = new Logger('guzzle');
$logger->pushHandler(new StreamHandler('/path/to/your.log', Logger::DEBUG));

$client = new GuzzleHttp\Client([
    'base_uri' => 'http://httpbin.org',
    'handler' => GuzzleHttp\HandlerStack::create(
        new GuzzleHttp\Handler\CurlHandler(),
        new GuzzleHttp\Handler\LoggingHandler($logger)
    )
]);

$response = $client->get('/get');
```

The output of the example code will be a log file containing the request and response information.

## Code explanation


1. `use Monolog\Logger;` and `use Monolog\Handler\StreamHandler;` - These lines import the Monolog library and the StreamHandler class.

2. `$logger = new Logger('guzzle');` - This line creates a new Logger instance with the name 'guzzle'.

3. `$logger->pushHandler(new StreamHandler('/path/to/your.log', Logger::DEBUG));` - This line adds a StreamHandler to the Logger instance, which will write the log messages to the specified file.

4. `new GuzzleHttp\Handler\LoggingHandler($logger)` - This line creates a LoggingHandler instance which will use the Logger instance to log the requests and responses.

5. `$client = new GuzzleHttp\Client([...])` - This line creates a new Guzzle client with the LoggingHandler added to the handler stack.

6. `$response = $client->get('/get');` - This line sends a GET request to httpbin.org and stores the response in the `$response` variable.

## Helpful links

- [Monolog Documentation](https://github.com/Seldaek/monolog)
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to use Monolog with Guzzle in PHP?](https://onelinerhub.com/php-guzzle/how-to-use-monolog-with-guzzle-in-php)