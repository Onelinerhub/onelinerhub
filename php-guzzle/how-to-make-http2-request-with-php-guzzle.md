# How to make HTTP2 request with PHP Guzzle?
// plain

Making an HTTP2 request with PHP Guzzle is easy. You just need to set the `HTTP_VERSION` option to `2.0` when creating the client.

```php
$client = new \GuzzleHttp\Client([
    'base_uri' => 'https://example.com',
    'http_version' => '2.0'
]);
```

The output of the above code will be a `GuzzleHttp\Client` instance with the HTTP version set to `2.0`.

1. `$client`: A `GuzzleHttp\Client` instance.
2. `base_uri`: The base URI of the client.
3. `http_version`: The HTTP version to use for requests.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to make HTTP2 request with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-make-http2-request-with-php-guzzle)