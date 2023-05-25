# How to convert a response to an array with PHP Guzzle?
// plain

To convert a response to an array with PHP Guzzle, you can use the `json()` method. This method will return the response body as a JSON-decoded array.

## Example code

```php
$client = new GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com/api/endpoint');
$data = $response->json();
```

## Output example

```
Array
(
    [0] => value1
    [1] => value2
    [2] => value3
)
```

## Code explanation

- `$client = new GuzzleHttp\Client();`: This creates a new Guzzle client.
- `$response = $client->request('GET', 'http://example.com/api/endpoint');`: This sends a GET request to the specified endpoint.
- `$data = $response->json();`: This converts the response body to a JSON-decoded array.

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to convert a response to an array with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-convert-a-response-to-an-array-with-php-guzzle)