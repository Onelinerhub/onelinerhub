# How to use PHP Guzzle Client?
// plain

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial to integrate with web services.

```
// Create a client with a base URI
$client = new GuzzleHttp\Client(['base_uri' => 'http://httpbin.org/']);

// Send a request to http://httpbin.org/get
$response = $client->request('GET', 'get');

echo $response->getStatusCode(); // 200
echo $response->getHeaderLine('content-type'); // 'application/json; charset=utf8'
echo $response->getBody(); // '{"type":"url","url":"http:\/\/httpbin.org\/get","args":{},"headers":{"host":"httpbin.org","accept":"*\/*"}}'
```

## Output example

```
200
application/json; charset=utf8
{"type":"url","url":"http:\/\/httpbin.org\/get","args":{},"headers":{"host":"httpbin.org","accept":"*\/*"}}
```

## Code explanation

- `$client = new GuzzleHttp\Client(['base_uri' => 'http://httpbin.org/']);` - creates a client with a base URI
- `$response = $client->request('GET', 'get');` - sends a request to http://httpbin.org/get
- `echo $response->getStatusCode();` - prints the status code of the response
- `echo $response->getHeaderLine('content-type');` - prints the content type of the response
- `echo $response->getBody();` - prints the body of the response

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Guzzle GitHub Repository](https://github.com/guzzle/guzzle)

onelinerhub: [How to use PHP Guzzle Client?](https://onelinerhub.com/php-guzzle/how-to-use-php-guzzle-client)