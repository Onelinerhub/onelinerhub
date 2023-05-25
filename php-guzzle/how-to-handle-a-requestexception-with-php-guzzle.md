# How to handle a RequestException with PHP Guzzle?
// plain

RequestException is an exception thrown when an error is encountered while processing an HTTP request. It can be handled with PHP Guzzle by using a try-catch block.

```
try {
    $client->request('GET', '/');
} catch (RequestException $e) {
    echo $e->getMessage();
}
```

The above code will catch any RequestException and print the error message.

## Code explanation

- `try {`: Start of the try-catch block
- `$client->request('GET', '/');`: Make a GET request to the root URL
- `catch (RequestException $e) {`: Catch any RequestException
- `echo $e->getMessage();`: Print the error message

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [PHP Exception Handling](https://www.php.net/manual/en/language.exceptions.php)

onelinerhub: [How to handle a RequestException with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-handle-a-requestexception-with-php-guzzle)