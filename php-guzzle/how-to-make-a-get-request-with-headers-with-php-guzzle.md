# How to make a GET request with headers with PHP Guzzle?
// plain

Using PHP Guzzle, you can make a GET request with headers by creating a `GuzzleHttp\Client` object and passing the headers as an array to the `request` method.

```php
$client = new GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com', [
    'headers' => [
        'X-Foo' => 'Bar',
        'X-Baz' => 'Qux'
    ]
]);
```

The output of the above code will be a `GuzzleHttp\Psr7\Response` object.

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a `GuzzleHttp\Client` object.
2. `$response = $client->request('GET', 'http://example.com', [` - This calls the `request` method on the `GuzzleHttp\Client` object, passing in the request type (`GET`), the URL (`http://example.com`), and an array of headers.
3. `'headers' => [` - This is the array of headers that will be sent with the request.
4. `'X-Foo' => 'Bar',` - This is an example of a header that will be sent with the request.
5. `]);` - This closes the array of headers and the `request` method.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to make a GET request with headers with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-make-a-get-request-with-headers-with-php-guzzle)