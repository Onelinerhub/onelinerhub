# PHP Guzzle usage example
// plain

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial to integrate with web services.

## Example code

```
<?php
$client = new GuzzleHttp\Client();
$res = $client->request('GET', 'https://api.github.com/user', [
    'auth' => ['user', 'pass']
]);
echo $res->getStatusCode();
// 200
echo $res->getHeader('content-type');
// 'application/json; charset=utf8'
echo $res->getBody();
// '{"id": 1420053, "name": "michael", "email": "michael@example.com"}'
?>
```

## Output example

```
200
application/json; charset=utf8
{"id": 1420053, "name": "michael", "email": "michael@example.com"}
```

## Code explanation

- `$client = new GuzzleHttp\Client();` - creates a new Guzzle client instance
- `$res = $client->request('GET', 'https://api.github.com/user', [ 'auth' => ['user', 'pass'] ]);` - sends a GET request to the specified URL with authentication credentials
- `echo $res->getStatusCode();` - prints the response status code
- `echo $res->getHeader('content-type');` - prints the response header
- `echo $res->getBody();` - prints the response body

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Guzzle GitHub Repository](https://github.com/guzzle/guzzle)

onelinerhub: [PHP Guzzle usage example](https://onelinerhub.com/php-guzzle/php-guzzle-usage-example)