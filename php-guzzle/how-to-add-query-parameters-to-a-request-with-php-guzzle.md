# How to add query parameters to a request with PHP Guzzle?
// plain

Query parameters can be added to a request with PHP Guzzle using the `query` method.

## Example code

```php
$client = new GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com', [
    'query' => [
        'foo' => 'bar',
        'baz' => 'qux'
    ]
]);
```

## Output example

```
GuzzleHttp\Psr7\Response {#7
  -reasonPhrase: "OK"
  -statusCode: 200
  -headers: array:7 [ …7]
  -headerLines: array:7 [ …7]
  -protocol: "1.1"
  -stream: GuzzleHttp\Psr7\Stream {#8 …}
}
```

## Code explanation

- `$client = new GuzzleHttp\Client();` - creates a new Guzzle client instance.
- `$response = $client->request('GET', 'http://example.com', [` - sends a GET request to the specified URL.
- `'query' => [` - specifies the query parameters to be added to the request.
- `'foo' => 'bar',` - adds the query parameter `foo` with the value `bar`.
- `'baz' => 'qux'` - adds the query parameter `baz` with the value `qux`.

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to add query parameters to a request with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-add-query-parameters-to-a-request-with-php-guzzle)