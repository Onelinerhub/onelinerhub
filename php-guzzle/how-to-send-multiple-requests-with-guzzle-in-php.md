# How to send multiple requests with Guzzle in PHP?
// plain

Guzzle is a PHP HTTP client that makes it easy to send multiple requests. To send multiple requests with Guzzle, you can use the `Pool` class. The `Pool` class allows you to send multiple requests concurrently and process the responses as they arrive.

## Example code

```php
$client = new GuzzleHttp\Client();
$requests = [
    'req1' => $client->getAsync('http://httpbin.org/get'),
    'req2' => $client->getAsync('http://httpbin.org/get?foo=bar'),
    'req3' => $client->getAsync('http://httpbin.org/get?baz=bam')
];

$pool = new GuzzleHttp\Pool($client, $requests);
$promise = $pool->promise();
$promise->wait();
```

## Output example

```
Array
(
    [req1] => GuzzleHttp\Psr7\Response Object
        (
            [reasonPhrase:GuzzleHttp\Psr7\Response:private] => OK
            [statusCode:GuzzleHttp\Psr7\Response:private] => 200
            [headers:GuzzleHttp\Psr7\Response:private] => Array
                (
                    [Date] => Array
                        (
                            [0] => Mon, 11 May 2020 11:45:45 GMT
                        )

                    [Content-Type] => Array
                        (
                            [0] => application/json
                        )

                    [Content-Length] => Array
                        (
                            [0] => 250
                        )

                    [Connection] => Array
                        (
                            [0] => keep-alive
                        )

                    [Server] => Array
                        (
                            [0] => gunicorn/19.9.0
                        )

                )

            [headerNames:GuzzleHttp\Psr7\Response:private] => Array
                (
                    [date] => Date
                    [content-type] => Content-Type
                    [content-length] => Content-Length
                    [connection] => Connection
                    [server] => Server
                )

            [protocol:GuzzleHttp\Psr7\Response:private] => 1.1
            [stream:GuzzleHttp\Psr7\Response:private] => GuzzleHttp\Psr7\Stream Object
                (
                    [stream:GuzzleHttp\Psr7\Stream:private] => Resource id #20
                    [size:GuzzleHttp\Psr7\Stream:private] =>
                    [seekable:GuzzleHttp\Psr7\Stream:private] => 1
                    [readable:GuzzleHttp\Psr7\Stream:private] => 1
                    [writable:GuzzleHttp\Psr7\Stream:private] => 1
                    [uri:GuzzleHttp\Psr7\Stream:private] => php://temp
                    [customMetadata:GuzzleHttp\Psr7\Stream:private] => Array
                        (
                        )

                )

        )

    [req2] => GuzzleHttp\Psr7\Response Object
        (
            [reasonPhrase:GuzzleHttp\Psr7\Response:private] => OK
            [statusCode:GuzzleHttp\Psr7\Response:private] => 200
            [headers:GuzzleHttp\Psr7\Response:private] => Array
                (
                    [Date] => Array
                        (
                            [0] => Mon, 11 May 2020 11:45:45 GMT
                        )

                    [Content-Type] => Array
                        (
                            [0] => application/json
                        )

                    [Content-Length] => Array
                        (
                            [0] => 250
                        )

                    [Connection] => Array
                        (
                            [0] => keep-alive
                        )

                    [Server] => Array
                        (
                            [0] => gunicorn/19.9.0
                        )

                )

            [headerNames:GuzzleHttp\Psr7\Response:private] => Array
                (
                    [date] => Date
                    [content-type] => Content-Type
                    [content-length] => Content-Length
                    [connection] => Connection
                    [server] => Server
                )

            [protocol:GuzzleHttp\Psr7\Response:private] => 1.1
            [stream:GuzzleHttp\Psr7\Response:private] => GuzzleHttp\Psr7\Stream Object
                (
                    [stream:GuzzleHttp\Psr7\Stream:private] => Resource id #21
                    [size:GuzzleHttp\Psr7\Stream:private] =>
                    [seekable:GuzzleHttp\Psr7\Stream:private] => 1
                    [readable:GuzzleHttp\Psr7\Stream:private] => 1
                    [writable:GuzzleHttp\Psr7\Stream:private] => 1
                    [uri:GuzzleHttp\Psr7\Stream:private] => php://temp
                    [customMetadata:GuzzleHttp\Psr7\Stream:private] => Array
                        (
                        )

                )

        )

    [req3] => GuzzleHttp\Psr7\Response Object
        (
            [reasonPhrase:GuzzleHttp\Psr7\Response:private] => OK
            [statusCode:GuzzleHttp\Psr7\Response:private] => 200
            [headers:GuzzleHttp\Psr7\Response:private] => Array
                (
                    [Date] => Array
                        (
                            [0] => Mon, 11 May 2020 11:45:45 GMT
                        )

                    [Content-Type] => Array
                        (
                            [0] => application/json
                        )

                    [Content-Length] => Array
                        (
                            [0] => 250
                        )

                    [Connection] => Array
                        (
                            [0] => keep-alive
                        )

                    [Server] => Array
                        (
                            [0] => gunicorn/19.9.0
                        )

                )

            [headerNames:GuzzleHttp\Psr7\Response:private] => Array
                (
                    [date] => Date
                    [content-type] => Content-Type
                    [content-length] => Content-Length
                    [connection] => Connection
                    [server] => Server
                )

            [protocol:GuzzleHttp\Psr7\Response:private] => 1.1
            [stream:GuzzleHttp\Psr7\Response:private] => GuzzleHttp\Psr7\Stream Object
                (
                    [stream:GuzzleHttp\Psr7\Stream:private] => Resource id #22
                    [size:GuzzleHttp\Psr7\Stream:private] =>
                    [seekable:GuzzleHttp\Psr7\Stream:private] => 1
                    [readable:GuzzleHttp\Psr7\Stream:private] => 1
                    [writable:GuzzleHttp\Psr7\Stream:private] => 1
                    [uri:GuzzleHttp\Psr7\Stream:private] => php://temp
                    [customMetadata:GuzzleHttp\Psr7\Stream:private] => Array
                        (
                        )

                )

        )

)
```

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client.
2. `$requests = [` - This creates an array of requests.
3. `'req1' => $client->getAsync('http://httpbin.org/get'),` - This adds a request to the array.
4. `$pool = new GuzzleHttp\Pool($client, $requests);` - This creates a new Pool object with the client and requests.
5. `$promise = $pool->promise();` - This creates a promise for the Pool object.
6. `$promise->wait();` - This waits for the promise to be fulfilled.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to send multiple requests with Guzzle in PHP?](https://onelinerhub.com/php-guzzle/how-to-send-multiple-requests-with-guzzle-in-php)