# How to install PHP Guzzle with Composer?
// plain

1. Install [Composer](https://getcomposer.org/download/) on your system.
2. Create a `composer.json` file in the root of your project and add the following code:
```json
{
    "require": {
        "guzzlehttp/guzzle": "^6.3"
    }
}
```
3. Run `composer install` in the root of your project.
4. Include the autoloader in your project:
```php
require 'vendor/autoload.php';
```
5. Use Guzzle in your project:
```php
$client = new \GuzzleHttp\Client();
$response = $client->request('GET', 'https://example.com');
echo $response->getStatusCode(); // 200
```

onelinerhub: [How to install PHP Guzzle with Composer?](https://onelinerhub.com/php-guzzle/how-to-install-php-guzzle-with-composer)