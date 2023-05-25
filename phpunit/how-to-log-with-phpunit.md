# How to log with PHPUnit?
// plain

PHPUnit is a unit testing framework for the PHP language. It can be used to log the results of tests.

To log with PHPUnit, you can use the `log` method of the `PHPUnit_Framework_TestCase` class. This method takes two parameters: the log message and the optional log type.

```php
<?php
$this->log('This is a log message', \PHPUnit_Framework_TestCase::LOG_INFO);
```

The output of the above code will be:
```
INFO This is a log message
```

The log type can be one of the following constants:
- `LOG_INFO`
- `LOG_WARNING`
- `LOG_ERROR`
- `LOG_RISK`
- `LOG_EXCEPTION`

For more information, please refer to the [PHPUnit documentation](https://phpunit.readthedocs.io/en/latest/).

onelinerhub: [How to log with PHPUnit?](https://onelinerhub.com/phpunit/how-to-log-with-phpunit)