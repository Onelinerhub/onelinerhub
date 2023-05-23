# How to use a proxy in PHP Symfony?
// plain

Using a proxy in PHP Symfony is easy. You can use the `GuzzleHttp` library to make requests through a proxy.

```php
$client = new \GuzzleHttp\Client([
    'proxy' => 'http://proxy.example.com:8080'
]);

$response = $client->request('GET', 'http://example.com');
```

The output of the above code will be the response from the `http://example.com` website.

1. `GuzzleHttp` library: This library is used to make requests through a proxy.
2. `proxy` option: This option is used to specify the proxy URL.
3. `request` method: This method is used to make a request to the specified URL.

## Helpful links

- [GuzzleHttp Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to use a proxy in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-a-proxy-in-php-symfony)