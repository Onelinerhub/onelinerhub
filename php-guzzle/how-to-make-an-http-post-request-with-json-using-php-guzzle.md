# How to make an HTTP POST request with JSON using PHP Guzzle?
// plain

Making an HTTP POST request with JSON using PHP Guzzle is easy. You can use the `post()` method of the Guzzle client to make a POST request. Here is an example code block:

```
$client = new GuzzleHttp\Client();
$response = $client->post('http://example.com/api/endpoint', [
    'json' => [
        'key1' => 'value1',
        'key2' => 'value2'
    ]
]);
```

The output of the example code will be an instance of `GuzzleHttp\Psr7\Response` class.

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client instance.
2. `$response = $client->post('http://example.com/api/endpoint', [` - This makes a POST request to the specified endpoint.
3. `'json' => [` - This specifies that the request body should be in JSON format.
4. `'key1' => 'value1',` - This is an example of a key-value pair that will be sent in the request body.
5. `]);` - This closes the array and sends the request.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Making a POST Request](http://docs.guzzlephp.org/en/stable/quickstart.html#making-a-request)

onelinerhub: [How to make an HTTP POST request with JSON using PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-make-an-http-post-request-with-json-using-php-guzzle)