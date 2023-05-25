# How to make an asynchronous send with PHP Guzzle?
// plain

Using PHP Guzzle, you can make asynchronous requests with the `requestAsync()` method.

## Example code

```php
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

- `$client = new GuzzleHttp\Client();`: creates a new Guzzle client.
- `$promise = $client->requestAsync('GET', 'http://www.example.com');`: makes an asynchronous request to the specified URL.
- `$promise->then(...)`: sets up a callback to be executed when the request is completed.
- `echo 'I completed! ' . $response->getBody();`: prints the response body when the request is successful.
- `echo 'I failed! ' . $exception->getMessage();`: prints the exception message when the request fails.

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to make an asynchronous send with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-make-an-asynchronous-send-with-php-guzzle)