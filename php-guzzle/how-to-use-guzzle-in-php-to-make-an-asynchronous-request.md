# How to use Guzzle in PHP to make an asynchronous request?
// plain

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial to integrate with web services. It can be used to make asynchronous requests in PHP.

## Example code

```
$client = new GuzzleHttp\Client();
$promise = $client->requestAsync('GET', 'http://www.example.com');
$promise->then(
    function ($response) {
        echo 'I completed! ' . $response->getBody();
    },
    function ($exception) {
        echo 'I failed! ' . $exception->getMessage();
    }
);
```

## Output example

```
I completed! <html>...</html>
```

## Code explanation

- `$client = new GuzzleHttp\Client();`: Create a new Guzzle client.
- `$promise = $client->requestAsync('GET', 'http://www.example.com');`: Make an asynchronous request to the given URL.
- `$promise->then(...)`: Register a callback to be executed when the request is completed.
- `function ($response) {...}`: Callback to be executed when the request is successful.
- `function ($exception) {...}`: Callback to be executed when the request fails.

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to use Guzzle in PHP to make an asynchronous request?](https://onelinerhub.com/php-guzzle/how-to-use-guzzle-in-php-to-make-an-asynchronous-request)