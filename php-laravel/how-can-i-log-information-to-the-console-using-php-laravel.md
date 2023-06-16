# How can I log information to the console using PHP Laravel?
// plain

Logging information to the console using PHP Laravel can be done by using the `Log` facade. The Log facade provides various logging levels such as `debug`, `info`, `notice`, `warning`, `error`, `critical`, `alert`, and `emergency`.

## Example code

```
Log::info('This is an info message');
```

## Output example

```
[2020-06-30 11:08:56] local.INFO: This is an info message
```

The code above will output an info message to the console. The code consists of the following parts:

- `Log` - the facade used to log the message.
- `info` - the logging level.
- `This is an info message` - the message that will be logged.

For more information see the [Laravel Logging Documentation](https://laravel.com/docs/7.x/logging).

onelinerhub: [How can I log information to the console using PHP Laravel?](https://onelinerhub.com/php-laravel/how-can-i-log-information-to-the-console-using-php-laravel)