# How to expect an error with PHPUnit?
// plain

PHPUnit is a unit testing framework for the PHP programming language. It can be used to expect errors in a program by writing test cases that check for expected errors.

For example, the following code block will expect an error when the function `divideByZero` is called:

```
<?php

class ErrorTest extends \PHPUnit\Framework\TestCase
{
    public function testDivideByZero()
    {
        $this->expectException(\DivisionByZeroError::class);
        divideByZero();
    }
}
```

When the test is run, the following output will be displayed:

```
PHPUnit 8.5.8 by Sebastian Bergmann and contributors.

E                                                                   1 / 1 (100%)

Time: 00:00.001, Memory: 6.00 MB

There was 1 error:

1) ErrorTest::testDivideByZero
DivisionByZeroError: Division by zero

/path/to/ErrorTest.php:7

ERRORS!
Tests: 1, Assertions: 0, Errors: 1.
```

## Code explanation


1. `$this->expectException(\DivisionByZeroError::class);` - This line tells PHPUnit to expect an error of type `DivisionByZeroError`.
2. `divideByZero();` - This line calls the function `divideByZero` which will cause the error.

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)
- [PHPUnit Tutorial](https://phpunit.de/manual/current/en/writing-tests-for-phpunit.html)

onelinerhub: [How to expect an error with PHPUnit?](https://onelinerhub.com/phpunit/how-to-expect-an-error-with-phpunit)