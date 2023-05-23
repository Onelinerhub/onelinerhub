# How to make an HTTP request in PHP Symfony?
// plain

Making an HTTP request in PHP Symfony is easy and straightforward.

## Example code

```
$client = new \GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com');
```

## Output example

```
GuzzleHttp\Psr7\Response {#741
  -reasonPhrase: 'OK'
  -statusCode: 200
  -headers: array:7 [ …7]
  -headerLines: array:7 [ …7]
  -protocol: '1.1'
  -stream: GuzzleHttp\Psr7\Stream {#742 …}
}
```

## Code explanation

- `$client = new \GuzzleHttp\Client();` - creates a new Guzzle client instance
- `$response = $client->request('GET', 'http://example.com');` - sends a GET request to the specified URL and stores the response in the `$response` variable

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Symfony Documentation](https://symfony.com/doc/current/index.html)

onelinerhub: [How to make an HTTP request in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-make-an-http-request-in-php-symfony)