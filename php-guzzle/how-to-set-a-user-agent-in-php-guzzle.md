# How to set a user agent in PHP Guzzle?
// plain

Setting a user agent in PHP Guzzle is easy. You can do it by passing a `User-Agent` header to the request.

```php
$client = new \GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com', [
    'headers' => [
        'User-Agent' => 'MyApp/1.0'
    ]
]);
```

The output of the above code will be a `GuzzleHttp\Psr7\Response` object.

## Code explanation


1. `$client = new \GuzzleHttp\Client();` - This creates a new Guzzle client.
2. `$response = $client->request('GET', 'http://example.com', [` - This sends a `GET` request to `http://example.com`.
3. `'headers' => [` - This sets the headers for the request.
4. `'User-Agent' => 'MyApp/1.0'` - This sets the `User-Agent` header to `MyApp/1.0`.
5. `]);` - This closes the array of headers.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [User Agent on MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)

onelinerhub: [How to set a user agent in PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-set-a-user-agent-in-php-guzzle)