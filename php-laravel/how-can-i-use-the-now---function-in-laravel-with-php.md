# How can I use the now() function in Laravel with PHP?
// plain

The `now()` function in Laravel is a helper function used to get the current timestamp. It is a wrapper around the PHP `date()` function and is a convenient way to get the current time.

## Example code

```
$now = now();
```

## Output example

```
2020-08-24 11:30:00
```

The `now()` function takes an optional parameter which is the timezone to use. By default, it uses the default timezone set in the `config/app.php` file. The following example sets the timezone to 'Asia/Tokyo':

## Example code

```
$now = now('Asia/Tokyo');
```

## Output example

```
2020-08-24 20:30:00
```

The `now()` function can also take an optional second parameter which is the date format to use. The following example sets the date format to 'Y-m-d H:i:s':

## Example code

```
$now = now('Asia/Tokyo', 'Y-m-d H:i:s');
```

## Output example

```
2020-08-24 20:30:00
```

## Helpful links
- [Laravel Documentation - Helpers - now()](https://laravel.com/docs/7.x/helpers#method-now)
- [PHP Manual - Date](https://www.php.net/manual/en/function.date.php)

onelinerhub: [How can I use the now() function in Laravel with PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-the-now---function-in-laravel-with-php)