# How can I print to the console using Laravel and PHP?
// plain

To print to the console using Laravel and PHP, you can use the `Log` facade. This facade provides various logging levels, such as `info`, `debug`, and `error`. Here is an example of how to use it:

```php
Log::info('This is an informational message');
```

The output of the above code would be:

```
[2020-04-13 10:20:30] local.INFO: This is an informational message
```

## Code explanation

- `Log`: This is the Log facade provided by Laravel.
- `info`: This is the logging level. There are various other logging levels available, such as `debug` and `error`.
- `This is an informational message`: This is the message that will be printed to the console.

Here are some ## Helpful links
- [Laravel Logging Documentation](https://laravel.com/docs/7.x/logging)
- [Laravel Logging Levels](https://laravel.com/docs/7.x/logging#logging-levels)

onelinerhub: [How can I print to the console using Laravel and PHP?](https://onelinerhub.com/php-laravel/how-can-i-print-to-the-console-using-laravel-and-php)