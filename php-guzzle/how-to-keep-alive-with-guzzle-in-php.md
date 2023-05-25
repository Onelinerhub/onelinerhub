# How to keep alive with Guzzle in PHP?
// plain

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial to integrate with web services. To keep alive with Guzzle in PHP, you can use the `Connection: keep-alive` header.

```php
$client = new GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com', [
    'headers' => [
        'Connection' => 'keep-alive'
    ]
]);
```

The output of the above code will be an instance of `GuzzleHttp\Psr7\Response` class.

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new instance of the Guzzle client.
2. `$response = $client->request('GET', 'http://example.com', [` - This sends a GET request to the specified URL.
3. `'headers' => [` - This is an array of headers to be sent with the request.
4. `'Connection' => 'keep-alive'` - This sets the `Connection` header to `keep-alive`.
5. `]);` - This closes the array of headers and the request options.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [HTTP/1.1 RFC](https://tools.ietf.org/html/rfc2616#section-14.10)

onelinerhub: [How to keep alive with Guzzle in PHP?](https://onelinerhub.com/php-guzzle/how-to-keep-alive-with-guzzle-in-php)