# How do I hash a password using PHP and Laravel?
// plain

Hashing a password using PHP and Laravel is a simple process. You can use the `Hash::make()` method provided by the Laravel framework.

## Example code

```php
$hashedPassword = Hash::make('password');
```

This will generate a hashed version of the password string provided.

## Code explanation

- `Hash::make()` - This is the method provided by Laravel which will generate a hashed version of the password string.
- `password` - This is the string which you want to hash.

The output of the above code will be a hashed version of the `password` string.

## Helpful links
- [Laravel Documentation - Hashing](https://laravel.com/docs/7.x/hashing)

onelinerhub: [How do I hash a password using PHP and Laravel?](https://onelinerhub.com/php-laravel/how-do-i-hash-a-password-using-php-and-laravel)