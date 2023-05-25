# How to catch a PHP Guzzle exception?
// plain

To catch a PHP Guzzle exception, you can use a `try/catch` block.

```php
try {
    // code that may throw an exception
} catch (GuzzleException $e) {
    // handle exception
}
```

## Code explanation


- `try`: This is the start of the `try/catch` block.
- `// code that may throw an exception`: This is the code that may throw an exception.
- `catch (GuzzleException $e)`: This is the part where you catch the GuzzleException.
- `// handle exception`: This is the part where you handle the exception.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [PHP Exceptions](https://www.php.net/manual/en/language.exceptions.php)

onelinerhub: [How to catch a PHP Guzzle exception?](https://onelinerhub.com/php-guzzle/how-to-catch-a-php-guzzle-exception)