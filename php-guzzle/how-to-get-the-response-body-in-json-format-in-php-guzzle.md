# How to get the response body in JSON format in PHP Guzzle?
// plain

To get the response body in JSON format in PHP Guzzle, you can use the `json()` method. This method will return the response body as a JSON object.

## Example code

```
$client = new GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com/api/v1/users');
$data = $response->json();
```

## Output example

```
[
    {
        "id": 1,
        "name": "John Doe"
    },
    {
        "id": 2,
        "name": "Jane Doe"
    }
]
```

## Code explanation

- `$client = new GuzzleHttp\Client();`: creates a new Guzzle client.
- `$response = $client->request('GET', 'http://example.com/api/v1/users');`: sends a GET request to the specified URL and stores the response in the `$response` variable.
- `$data = $response->json();`: parses the response body as a JSON object and stores it in the `$data` variable.

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to get the response body in JSON format in PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-get-the-response-body-in-json-format-in-php-guzzle)