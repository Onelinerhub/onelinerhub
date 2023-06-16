# How do I print an array in Laravel using PHP?
// plain

To print an array in Laravel using PHP, you can use the `print_r()` function. This function will output the contents of an array in a human readable format.

For example, if you have an array called `$myArray`:

```php
$myArray = [
    'name' => 'John',
    'age' => 18
];
```

You can print the contents of this array with:

```php
print_r($myArray);
```

The output of this code would be:

```
Array
(
    [name] => John
    [age] => 18
)
```

You can also use the `var_dump()` function to get more detailed information about the array, such as its data types.

You can find more information about these functions in the [PHP manual](https://www.php.net/manual/en/function.print-r.php).

onelinerhub: [How do I print an array in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-print-an-array-in-laravel-using-php)