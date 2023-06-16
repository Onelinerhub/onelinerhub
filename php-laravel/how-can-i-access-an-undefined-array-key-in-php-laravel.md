# How can I access an undefined array key in PHP Laravel?
// plain

In PHP Laravel, you can access an undefined array key by using the `array_key_exists()` function. This function will check if the specified key exists in the given array and returns a boolean value.

## Example

```
$array = array(
    'name' => 'John',
    'age' => 25
);

if(array_key_exists('address', $array)) {
    echo 'Key exists';
} else {
    echo 'Key does not exist';
}
```
## Output example

```
Key does not exist
```

The `array_key_exists()` function takes two parameters - the key to check and the array. If the key is found in the array, it will return `true`; otherwise, it will return `false`.

## Code explanation

- `$array`: an array containing two key-value pairs
- `array_key_exists()`: a function used to check if a key exists in the given array
- `if`: a conditional statement used to check the result of `array_key_exists()`
- `echo`: a function used to output the result of the check

## Helpful links
- [PHP: array_key_exists - Manual](https://www.php.net/manual/en/function.array-key-exists.php)
- [PHP if else Statement](https://www.w3schools.com/php/php_if_else.asp)
- [PHP echo Function](https://www.w3schools.com/php/func_string_echo.asp)

onelinerhub: [How can I access an undefined array key in PHP Laravel?](https://onelinerhub.com/php-laravel/how-can-i-access-an-undefined-array-key-in-php-laravel)