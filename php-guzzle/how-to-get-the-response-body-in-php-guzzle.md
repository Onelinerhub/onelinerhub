# How to get the response body in PHP Guzzle?
// plain

The response body in PHP Guzzle can be obtained using the `getBody()` method.

## Example code

```
$client = new \GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com');
$body = $response->getBody();
```

## Output example

```
GuzzleHttp\Psr7\Stream Object
(
    [stream:GuzzleHttp\Psr7\Stream:private] => Resource id #3
    [size:GuzzleHttp\Psr7\Stream:private] =>
    [seekable:GuzzleHttp\Psr7\Stream:private] => 1
    [readable:GuzzleHttp\Psr7\Stream:private] => 1
    [writable:GuzzleHttp\Psr7\Stream:private] => 1
    [uri:GuzzleHttp\Psr7\Stream:private] => php://temp
    [customMetadata:GuzzleHttp\Psr7\Stream:private] => Array
        (
        )

)
```

## Code explanation

- `$client = new \GuzzleHttp\Client();` - creates a new Guzzle client
- `$response = $client->request('GET', 'http://example.com');` - sends a GET request to the specified URL
- `$body = $response->getBody();` - gets the response body

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to get the response body in PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-get-the-response-body-in-php-guzzle)