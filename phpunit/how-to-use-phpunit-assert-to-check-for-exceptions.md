# How to use PHPUnit assert to check for exceptions?
// plain

PHPUnit provides a convenient way to check for exceptions using the `assertThrow()` method. This method takes two parameters: the expected exception class and a callable that should throw the exception.

```
<?php

use PHPUnit\Framework\TestCase;

class ExceptionTest extends TestCase
{
    public function testException()
    {
        $this->expectException(\InvalidArgumentException::class);
        throw new \InvalidArgumentException('Exception message');
    }
}
```

The above example will throw an `\InvalidArgumentException` and the test will pass.

## Code explanation


1. `use PHPUnit\Framework\TestCase;` - imports the TestCase class from the PHPUnit framework.
2. `$this->expectException(\InvalidArgumentException::class);` - sets the expected exception class.
3. `throw new \InvalidArgumentException('Exception message');` - throws the exception.

## Helpful links

- [PHPUnit Documentation - Assertions](https://phpunit.readthedocs.io/en/9.2/assertions.html#assertthrows)

onelinerhub: [How to use PHPUnit assert to check for exceptions?](https://onelinerhub.com/phpunit/how-to-use-phpunit-assert-to-check-for-exceptions)