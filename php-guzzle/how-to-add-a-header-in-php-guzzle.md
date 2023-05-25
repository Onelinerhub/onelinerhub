# How to add a header in PHP Guzzle?
// plain

Adding a header in PHP Guzzle is a simple process. To do this, you need to create a `GuzzleHttp\Client` object and pass an array of headers to the `request` method.

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


1. `GuzzleHttp\Client`: This is the class used to create a client object.
2. `request`: This is the method used to make a request.
3. `headers`: This is the array of headers to be sent with the request.
4. `X-Foo` and `X-Baz`: These are the header names.
5. `Bar` and `Qux`: These are the header values.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to add a header in PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-add-a-header-in-php-guzzle)