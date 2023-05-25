# How to expect an exception in PHPUnit?
// plain

Expecting an exception in PHPUnit is done using the `expectException()` method. This method takes a single parameter, which is the expected exception class name.

```
<?php

use PHPUnit\Framework\TestCase;

class ExceptionTest extends TestCase
{
    public function testException()
    {
        $this->expectException('Exception');
        throw new Exception();
    }
}
```

The output of the above code will be:

```
OK (1 test, 1 assertion)
```

## Code explanation


1. `use PHPUnit\Framework\TestCase;` - This imports the TestCase class from the PHPUnit framework.
2. `$this->expectException('Exception');` - This is the method used to expect an exception. It takes the expected exception class name as a parameter.
3. `throw new Exception();` - This is the line that throws the exception.

## Helpful links

- [PHPUnit Documentation - Expecting Exceptions](https://phpunit.readthedocs.io/en/9.2/writing-tests-for-phpunit.html#expecting-exceptions)

onelinerhub: [How to expect an exception in PHPUnit?](https://onelinerhub.com/phpunit/how-to-expect-an-exception-in-phpunit)