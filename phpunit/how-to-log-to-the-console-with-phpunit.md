# How to log to the console with PHPUnit?
// plain

Logging to the console with PHPUnit is possible using the `write` method of the `PHPUnit_TextUI_ResultPrinter` class.

## Example code

```
$printer = new PHPUnit_TextUI_ResultPrinter();
$printer->write("This is a log message");
```

## Output example

```
This is a log message
```

The code consists of two parts:

1. Creating an instance of the `PHPUnit_TextUI_ResultPrinter` class:
```
$printer = new PHPUnit_TextUI_ResultPrinter();
```

2. Writing a log message to the console using the `write` method of the `PHPUnit_TextUI_ResultPrinter` class:
```
$printer->write("This is a log message");
```

For more information, please refer to the [PHPUnit documentation](https://phpunit.readthedocs.io/en/9.2/textui.html).

onelinerhub: [How to log to the console with PHPUnit?](https://onelinerhub.com/phpunit/how-to-log-to-the-console-with-phpunit)