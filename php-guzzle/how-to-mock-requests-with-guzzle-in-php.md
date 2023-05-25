# How to mock requests with Guzzle in PHP?
// plain

Mocking requests with Guzzle in PHP is a great way to test your application without making actual requests.

```php
$mock = new \GuzzleHttp\Handler\MockHandler([
    new \GuzzleHttp\Psr7\Response(200, [], '{"foo": "bar"}'),
]);

$handler = \GuzzleHttp\HandlerStack::create($mock);
$client = new \GuzzleHttp\Client(['handler' => $handler]);

$response = $client->request('GET', 'http://example.com');

echo $response->getBody();
```

## Output example

```
{"foo": "bar"}
```

## Code explanation

- `$mock`: creates a new MockHandler instance with the given responses.
- `$handler`: creates a HandlerStack instance with the given handler.
- `$client`: creates a new Client instance with the given handler.
- `$response`: sends a request to the given URL and returns a response.
- `getBody()`: returns the body of the response.

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Mocking Requests with Guzzle](https://www.sitepoint.com/mocking-requests-guzzle/)

onelinerhub: [How to mock requests with Guzzle in PHP?](https://onelinerhub.com/php-guzzle/how-to-mock-requests-with-guzzle-in-php)