# How can I view the error log for my Laravel application using PHP?
// plain

In order to view the error log for your Laravel application using PHP, you can use the built-in Monolog library. Monolog is a logging library for PHP applications, and is included in the Laravel framework.

To view the log, you can use the following code snippet:

```
use Monolog\Logger;
use Monolog\Handler\StreamHandler;

// create a log channel
$log = new Logger('name');
$log->pushHandler(new StreamHandler('path/to/your.log', Logger::WARNING));

// add records to the log
$log->warning('Foo');
$log->error('Bar');
```

The output of the above code will be two new entries in the log file:

```
[2018-05-30 08:30:00] name.WARNING: Foo
[2018-05-30 08:30:00] name.ERROR: Bar
```

## Code explanation


1. `use Monolog\Logger;` - this imports the Monolog Logger class into the current namespace.
2. `use Monolog\Handler\StreamHandler;` - this imports the Monolog StreamHandler class into the current namespace.
3. `$log = new Logger('name');` - this creates a new Logger instance with the name 'name'.
4. `$log->pushHandler(new StreamHandler('path/to/your.log', Logger::WARNING));` - this sets the log file path and the minimum log level to be logged.
5. `$log->warning('Foo');` - this adds a log entry with the level 'warning' and the message 'Foo'.
6. `$log->error('Bar');` - this adds a log entry with the level 'error' and the message 'Bar'.

For more information, please see the [Monolog Documentation](https://github.com/Seldaek/monolog).

onelinerhub: [How can I view the error log for my Laravel application using PHP?](https://onelinerhub.com/php-laravel/how-can-i-view-the-error-log-for-my-laravel-application-using-php)