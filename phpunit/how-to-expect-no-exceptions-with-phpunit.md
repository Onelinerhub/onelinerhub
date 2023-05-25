# How to expect no exceptions with PHPUnit?
// plain

PHPUnit is a popular unit testing framework for PHP. It can be used to test code and ensure that it works as expected without any exceptions.

To expect no exceptions with PHPUnit, you can use the `@expectedException` annotation. This annotation allows you to specify the type of exception that you expect to be thrown.

```
<?php

class MyTest extends \PHPUnit_Framework_TestCase
{
    /**
     * @expectedException InvalidArgumentException
     */
    public function testException()
    {
        throw new InvalidArgumentException();
    }
}
```

The code above will pass the test if an `InvalidArgumentException` is thrown.

- `@expectedException` annotation: used to specify the type of exception that you expect to be thrown
- `InvalidArgumentException`: the type of exception that is expected to be thrown

## Helpful links

- [PHPUnit Documentation](https://phpunit.de/documentation.html)
- [PHPUnit @expectedException Annotation](https://phpunit.readthedocs.io/en/latest/annotations.html#expectexception)

onelinerhub: [How to expect no exceptions with PHPUnit?](https://onelinerhub.com/phpunit/how-to-expect-no-exceptions-with-phpunit)