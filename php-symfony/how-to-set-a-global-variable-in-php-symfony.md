# How to set a global variable in PHP Symfony?
// plain

A global variable in PHP Symfony can be set using the `$GLOBALS` array. This array is a superglobal variable which is available in all scopes throughout a script.

```php
$GLOBALS['my_var'] = 'Hello World';
echo $GLOBALS['my_var'];
```

## Output example

```
Hello World
```

- `$GLOBALS`: This is a superglobal array which is available in all scopes throughout a script.
- `$GLOBALS['my_var']`: This is the global variable which is being set.
- `'Hello World'`: This is the value of the global variable.
- `echo $GLOBALS['my_var']`: This is used to output the value of the global variable.

## Helpful links
- [PHP: $GLOBALS](https://www.php.net/manual/en/reserved.variables.globals.php)

onelinerhub: [How to set a global variable in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-set-a-global-variable-in-php-symfony)