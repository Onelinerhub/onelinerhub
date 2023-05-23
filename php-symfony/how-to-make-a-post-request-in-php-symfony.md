# How to make a POST request in PHP Symfony?
// plain

Making a POST request in PHP Symfony is easy and straightforward.

## Example code

```
$client = new Client();
$response = $client->request('POST', 'http://example.com/api/endpoint', [
    'form_params' => [
        'param1' => 'value1',
        'param2' => 'value2',
    ]
]);
```

## Output example

```
GuzzleHttp\Psr7\Response {#741
  -reasonPhrase: "OK"
  -statusCode: 200
  -headers: array:7 [
    "Date" => array:1 [
      0 => "Mon, 15 Jun 2020 13:45:00 GMT"
    ]
    "Server" => array:1 [
      0 => "Apache/2.4.18 (Ubuntu)"
    ]
    "X-Powered-By" => array:1 [
      0 => "PHP/7.2.24-0ubuntu0.18.04.4"
    ]
    "Cache-Control" => array:1 [
      0 => "no-cache, private"
    ]
    "Content-Length" => array:1 [
      0 => "1234"
    ]
    "Content-Type" => array:1 [
      0 => "application/json"
    ]
  ]
  -headerNames: array:7 [
    "date" => "Date"
    "server" => "Server"
    "x-powered-by" => "X-Powered-By"
    "cache-control" => "Cache-Control"
    "content-length" => "Content-Length"
    "content-type" => "Content-Type"
  ]
  -protocol: "1.1"
  -stream: Stream {#742
    -stream: stream resource @7
    -size: null
    -seekable: true
    -readable: true
    -writable: true
    -uri: "php://temp"
    -customMetadata: []
  }
}
```

## Code explanation

- `$client = new Client();` - creates a new instance of the Client class from the GuzzleHttp library.
- `$response = $client->request('POST', 'http://example.com/api/endpoint', [` - sends a POST request to the specified endpoint.
- `'form_params' => [` - specifies the parameters to be sent in the request body.
- `'param1' => 'value1',` - sets the value of the parameter `param1` to `value1`.
- `$response` - stores the response from the server.

## Helpful links
- [GuzzleHttp documentation](http://docs.guzzlephp.org/en/stable/)
- [Symfony documentation](https://symfony.com/doc/current/index.html)

onelinerhub: [How to make a POST request in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-make-a-post-request-in-php-symfony)