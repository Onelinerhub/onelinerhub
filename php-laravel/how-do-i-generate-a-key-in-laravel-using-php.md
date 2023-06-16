# How do I generate a key in Laravel using PHP?
// plain

Generating a key in Laravel using PHP is a simple process. Here is an example of how to do it:

```
// Generate the key
$key = str_random(32);

// Output the key
echo $key;
```

This will output a random 32 character string, such as `S8gxXG6h3Lhx9V4BjRmVJm6KU8dQqEKW`.

The code consists of two parts:
- `str_random(32)`: This is a Laravel helper function which generates a random string with the specified length (in this case, 32 characters).
- `echo $key`: This outputs the generated key to the screen.

For more information, see the [Laravel Documentation](https://laravel.com/docs/5.7/helpers#method-str-random).

onelinerhub: [How do I generate a key in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-generate-a-key-in-laravel-using-php)