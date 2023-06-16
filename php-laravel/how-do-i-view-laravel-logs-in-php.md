# How do I view Laravel logs in PHP?
// plain

To view Laravel logs in PHP, you can use the `Log::info()` method. It will log a message to the log file located in the `storage/logs` directory. For example,

```php
Log::info('This is an informational message');
```

This will write the message `This is an informational message` to the log file.

To view the log file, you can use the `tail` command. For example,

```
tail -f storage/logs/laravel.log
```

This will output the contents of the log file in real time.

The following are the parts of the code:

- `Log::info()` - This is a static method of the `Log` class that is used to log a message to the log file.
- `tail` - This is a command line utility that is used to view the contents of a log file in real time.

## Helpful links

- [Laravel Logging](https://laravel.com/docs/5.8/logging)
- [Linux tail command](https://linuxize.com/post/linux-tail-command/)

onelinerhub: [How do I view Laravel logs in PHP?](https://onelinerhub.com/php-laravel/how-do-i-view-laravel-logs-in-php)