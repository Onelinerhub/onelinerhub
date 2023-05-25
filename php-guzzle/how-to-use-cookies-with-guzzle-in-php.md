# How to use cookies with Guzzle in PHP?
// plain

Cookies can be used with Guzzle in PHP by setting the `Cookie` header in the request.

```php
$client = new GuzzleHttp\Client();
$response = $client->request('GET', 'http://httpbin.org/cookies', [
    'headers' => [
        'Cookie' => 'foo=bar; bar=baz'
    ]
]);
```

The output of the above code will be a response object containing the cookies sent in the request.

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client object.
2. `'headers' => [ 'Cookie' => 'foo=bar; bar=baz' ]` - This sets the `Cookie` header in the request with the cookies `foo=bar` and `bar=baz`.
3. `$response = $client->request('GET', 'http://httpbin.org/cookies', [ ... ])` - This sends the request to the specified URL with the `Cookie` header set.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to use cookies with Guzzle in PHP?](https://onelinerhub.com/php-guzzle/how-to-use-cookies-with-guzzle-in-php)