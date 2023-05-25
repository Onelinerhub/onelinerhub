# How to use Promises with PHP Guzzle (with an example)?
// plain

Promises are a way to handle asynchronous operations in PHP Guzzle. Promises allow you to write code that is more readable and easier to maintain.

## Example code

```php
$client = new \GuzzleHttp\Client();
$promise = $client->getAsync('http://www.example.com');
$promise->then(
    function ($response) {
        echo $response->getStatusCode();
    },
    function ($exception) {
        echo $exception->getMessage();
    }
);
```

## Output example

```
200
```

## Code explanation

- `$client = new \GuzzleHttp\Client();` - creates a new Guzzle client
- `$promise = $client->getAsync('http://www.example.com');` - creates a promise for an asynchronous GET request
- `$promise->then(...)` - registers a callback to be executed when the promise is fulfilled
- `function ($response) { ... }` - callback to be executed when the promise is fulfilled
- `function ($exception) { ... }` - callback to be executed when the promise is rejected

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Promises in PHP](https://promisesaplus.com/)

onelinerhub: [How to use Promises with PHP Guzzle (with an example)?](https://onelinerhub.com/php-guzzle/how-to-use-promises-with-php-guzzle--with-an-example-)