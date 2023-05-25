# How to set a timeout for a request with PHP Guzzle?
// plain

You can set a timeout for a request with PHP Guzzle by using the `timeout` option in the request options array.

## Example code

```php
$client = new GuzzleHttp\Client();
$response = $client->request('GET', 'http://www.example.com', [
    'timeout' => 2.0,
]);
```

## Output example

```
GuzzleHttp\Psr7\Response
```

## Code explanation

- `$client = new GuzzleHttp\Client();` - creates a new Guzzle client instance
- `$client->request('GET', 'http://www.example.com', [` - sends a GET request to the specified URL
- `'timeout' => 2.0,` - sets the timeout for the request to 2 seconds
- `]);` - closes the request options array

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to set a timeout for a request with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-set-a-timeout-for-a-request-with-php-guzzle)