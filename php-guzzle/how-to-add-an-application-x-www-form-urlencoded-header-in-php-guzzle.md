# How to add an application/x-www-form-urlencoded header in PHP Guzzle?
// plain

Adding an application/x-www-form-urlencoded header in PHP Guzzle can be done using the `setHeader` method.

## Example code

```
$client = new \GuzzleHttp\Client();
$client->setHeader('Content-Type', 'application/x-www-form-urlencoded');
```

The code above creates a new Guzzle client and sets the header `Content-Type` to `application/x-www-form-urlencoded`.

## Code explanation

- `$client = new \GuzzleHttp\Client();` - creates a new Guzzle client
- `$client->setHeader('Content-Type', 'application/x-www-form-urlencoded');` - sets the header `Content-Type` to `application/x-www-form-urlencoded`

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to add an application/x-www-form-urlencoded header in PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-add-an-application-x-www-form-urlencoded-header-in-php-guzzle)