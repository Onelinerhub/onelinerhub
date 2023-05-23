# How to create an HTTP client in PHP Symfony?
// plain

Creating an HTTP client in PHP Symfony is easy and straightforward.

```php
$client = new \GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com');
```

The above code will create an HTTP client and make a GET request to the URL `http://example.com`.

1. `$client = new \GuzzleHttp\Client();` - This line creates a new instance of the GuzzleHttp Client.
2. `$response = $client->request('GET', 'http://example.com');` - This line makes a GET request to the URL `http://example.com` and stores the response in the `$response` variable.

## Helpful links

- [GuzzleHttp Documentation](http://docs.guzzlephp.org/en/stable/)
- [Symfony Documentation](https://symfony.com/doc/current/index.html)

onelinerhub: [How to create an HTTP client in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-create-an-http-client-in-php-symfony)