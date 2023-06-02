# xception

How can I handle a FileException in PHP Omnipay?
// plain

In order to handle a FileException in PHP Omnipay, you can use the `try-catch` statement to catch the exception and then handle it accordingly.

## Example code

```
try {
    // code that might throw an exception
} catch (FileException $e) {
    echo 'FileException: ' . $e->getMessage();
}
```

## Output example

```
FileException: File not found
```

The code above consists of the following parts:
- `try` - this statement will try to execute the code inside the block, and if an exception is thrown, the code inside the `catch` block will be executed.
- `catch` - this statement will catch the thrown exception and store it in the `$e` variable.
- `echo` - this statement will print out the exception message.

## Helpful links
- [PHP try-catch](https://www.php.net/manual/en/language.exceptions.php)
- [Omnipay FileException](https://github.com/thephpleague/omnipay/blob/master/src/Exception/FileException.php)

onelinerhub: [xception

How can I handle a FileException in PHP Omnipay?](https://onelinerhub.com/php-omnipay/xception--how-can-i-handle-a-fileexception-in-php-omnipay)