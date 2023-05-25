# How to use PHP Guzzle to make a batch request?
// plain

PHP Guzzle can be used to make batch requests. This is done by creating an array of requests and passing it to the `send()` method of the `GuzzleHttp\Client` class.

```php
$client = new GuzzleHttp\Client();
$requests = [
    'req1' => $client->getAsync('http://httpbin.org/get'),
    'req2' => $client->getAsync('http://httpbin.org/get?foo=bar'),
    'req3' => $client->getAsync('http://httpbin.org/get?baz=bam')
];
$results = GuzzleHttp\Promise\unwrap($requests);
```

The output of the above code will be an array of responses:

```
Array
(
    [req1] => GuzzleHttp\Psr7\Response Object
        (
            [reasonPhrase:GuzzleHttp\Psr7\Response:private] => OK
            ...
        )
    [req2] => GuzzleHttp\Psr7\Response Object
        (
            [reasonPhrase:GuzzleHttp\Psr7\Response:private] => OK
            ...
        )
    [req3] => GuzzleHttp\Psr7\Response Object
        (
            [reasonPhrase:GuzzleHttp\Psr7\Response:private] => OK
            ...
        )
)
```

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new instance of the `GuzzleHttp\Client` class.
2. `$requests = [ ... ]` - This creates an array of requests.
3. `$results = GuzzleHttp\Promise\unwrap($requests);` - This sends the requests and returns an array of responses.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to use PHP Guzzle to make a batch request?
](https://onelinerhub.com/php-guzzle/how-to-use-php-guzzle-to-make-a-batch-request)
