# How to retry requests with PHP Guzzle?
// plain

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial to integrate with web services. To retry requests with Guzzle, you can use the `retry` middleware.

```php
$client = new \GuzzleHttp\Client();
$client->getConfig('handler')->push(\GuzzleHttp\Middleware::retry(
    $retryDecider,
    $retryDelay
));
```

The `retry` middleware takes two parameters:

- `$retryDecider`: A callable that accepts the number of retries, a request, response, and exception (when available) and returns true if the request is to be retried.
- `$retryDelay`: A callable that accepts the number of retries and returns the number of milliseconds to delay.

For more information, see the [Guzzle documentation](http://docs.guzzlephp.org/en/stable/quickstart.html#retrying-requests).

onelinerhub: [How to retry requests with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-retry-requests-with-php-guzzle)