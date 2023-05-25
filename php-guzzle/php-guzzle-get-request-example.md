# PHP Guzzle get request example
// plain

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial to integrate with web services. Here is an example of how to use Guzzle to make a GET request:

```
<?php
$client = new GuzzleHttp\Client();
$res = $client->request('GET', 'https://api.github.com/user', [
    'auth' => ['user', 'pass']
]);
echo $res->getStatusCode();
// "200"
echo $res->getHeader('content-type');
// 'application/json; charset=utf8'
echo $res->getBody();
// {"type":"User"...'
?>
```

The code above will make a GET request to the URL `https://api.github.com/user` with authentication credentials `user` and `pass`. The response will be stored in the `$res` variable. The status code, header and body of the response can be accessed using the `getStatusCode()`, `getHeader()` and `getBody()` methods respectively.

Parts of the code:

- `$client = new GuzzleHttp\Client();`: This creates a new Guzzle client.
- `$res = $client->request('GET', 'https://api.github.com/user', [ 'auth' => ['user', 'pass'] ]);`: This makes a GET request to the URL `https://api.github.com/user` with authentication credentials `user` and `pass`.
- `echo $res->getStatusCode();`: This prints the status code of the response.
- `echo $res->getHeader('content-type');`: This prints the value of the `content-type` header of the response.
- `echo $res->getBody();`: This prints the body of the response.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [PHP Guzzle get request example](https://onelinerhub.com/php-guzzle/php-guzzle-get-request-example)