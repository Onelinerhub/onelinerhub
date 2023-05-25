# How to use PHP Guzzle to make an API request?
// plain

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial to integrate with web services.

To make an API request with Guzzle, you need to create a client and then make a request.

## Example code

```
$client = new GuzzleHttp\Client();
$res = $client->request('GET', 'https://api.example.com/endpoint');
```

## Output example

```
GuzzleHttp\Psr7\Response {#200
  -reasonPhrase: "OK"
  -statusCode: 200
  -headers: array:7 [ …7]
  -headerLines: array:7 [ …7]
  -protocol: "1.1"
  -stream: GuzzleHttp\Psr7\Stream {#201 …}
}
```

## Code explanation

- `$client = new GuzzleHttp\Client();` creates a new Guzzle client.
- `$res = $client->request('GET', 'https://api.example.com/endpoint');` makes a GET request to the specified endpoint.

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Guzzle GitHub Repository](https://github.com/guzzle/guzzle)

onelinerhub: [How to use PHP Guzzle to make an API request?](https://onelinerhub.com/php-guzzle/how-to-use-php-guzzle-to-make-an-api-request)