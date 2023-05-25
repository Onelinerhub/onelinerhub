# How to get the body in PHP Guzzle?
// plain

The body of a response in PHP Guzzle can be obtained using the `getBody()` method.

## Example code

```php
$client = new GuzzleHttp\Client();
$res = $client->request('GET', 'http://www.example.com');
echo $res->getBody();
```

## Output example

```
<html>
    <head>
        <title>Example Domain</title>
    </head>
    <body>
        <h1>Example Domain</h1>
        <p>This domain is established to be used for illustrative examples in documents. You may use this
        domain in examples without prior coordination or asking for permission.</p>
    </body>
</html>
```

## Code explanation

- `$client = new GuzzleHttp\Client();`: This creates a new Guzzle client.
- `$res = $client->request('GET', 'http://www.example.com');`: This sends a GET request to the specified URL.
- `echo $res->getBody();`: This prints the body of the response.

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to get the body in PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-get-the-body-in-php-guzzle)