# How to handle a timeout exception with PHP Guzzle?
// plain

To handle a timeout exception with PHP Guzzle, you can use the `timeout` option in the request options array. This option allows you to specify the maximum number of seconds to wait for a response before timing out. For example:

```php
$client = new GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com', [
    'timeout' => 10
]);
```

This will set the timeout to 10 seconds. If the response is not received within 10 seconds, a `GuzzleHttp\Exception\ConnectException` will be thrown.

You can also set a default timeout for all requests by passing the `timeout` option to the constructor:

```php
$client = new GuzzleHttp\Client([
    'timeout' => 10
]);
```

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client instance.
2. `$response = $client->request('GET', 'http://example.com', [ 'timeout' => 10 ]);` - This sends a GET request to the specified URL with a timeout of 10 seconds.
3. `$client = new GuzzleHttp\Client([ 'timeout' => 10 ]);` - This creates a new Guzzle client instance with a default timeout of 10 seconds.

No relevant links.

onelinerhub: [How to handle a timeout exception with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-handle-a-timeout-exception-with-php-guzzle)