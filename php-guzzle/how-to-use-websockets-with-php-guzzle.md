# How to use websockets with PHP Guzzle?
// plain

Websockets can be used with PHP Guzzle to create real-time applications. To use websockets with PHP Guzzle, you need to install the Guzzle websocket library.

## Example code

```
$client = new \GuzzleHttp\Client();
$websocket = new \GuzzleHttp\Psr7\Uri('ws://localhost:8080');
$client->request('GET', $websocket);
```

The code above creates a new Guzzle client and a new websocket Uri. The request method is then used to connect to the websocket.

## Code explanation

- `$client = new \GuzzleHttp\Client();` - creates a new Guzzle client
- `$websocket = new \GuzzleHttp\Psr7\Uri('ws://localhost:8080');` - creates a new websocket Uri
- `$client->request('GET', $websocket);` - connects to the websocket

## Helpful links
- [Guzzle websocket library](https://github.com/guzzle/websocket-subscriber)
- [Guzzle documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to use websockets with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-use-websockets-with-php-guzzle)