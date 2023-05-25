# How to stream with PHP Guzzle?
// plain

Streaming with PHP Guzzle is a great way to make HTTP requests and receive responses in a continuous stream. To stream with Guzzle, you need to use the `stream` option when making a request.

```php
$client = new GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com', [
    'stream' => true
]);
```

The response will be a `GuzzleHttp\Psr7\Stream` object, which can be used to read the response body in chunks.

```php
$body = $response->getBody();
while (!$body->eof()) {
    echo $body->read(1024);
}
```

The code above will read the response body in chunks of 1024 bytes and echo them out.

The parts of the code are:

- `$client = new GuzzleHttp\Client();`: This creates a new Guzzle client.
- `$response = $client->request('GET', 'http://example.com', ['stream' => true]);`: This makes a GET request to the given URL with the `stream` option set to `true`.
- `$body = $response->getBody();`: This gets the response body as a `GuzzleHttp\Psr7\Stream` object.
- `while (!$body->eof()) {`: This starts a loop that will run until the end of the stream is reached.
- `echo $body->read(1024);`: This reads 1024 bytes from the stream and echoes them out.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/)
- [Streaming Responses](http://docs.guzzlephp.org/en/stable/request-options.html#stream)

onelinerhub: [How to stream with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-stream-with-php-guzzle)