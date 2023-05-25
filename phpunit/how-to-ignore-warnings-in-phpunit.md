# How to ignore warnings in PHPUnit?
// plain

You can ignore warnings in PHPUnit by using the `@expectedException` annotation. This annotation allows you to specify the type of exception that is expected to be thrown from a test.

For example:
```
/**
 * @expectedException PHPUnit_Framework_Error_Warning
 */
public function testSomething()
{
    // code that triggers a warning
}
```

The `@expectedException` annotation has two parts:

1. `PHPUnit_Framework_Error_Warning` - This is the type of exception that is expected to be thrown.
2. `testSomething()` - This is the name of the test that is expected to throw the exception.

The output of the example code will be:
```
OK (1 test, 1 assertion)
```

## Helpful links

- [PHPUnit Documentation - Exceptions](https://phpunit.readthedocs.io/en/9.2/writing-tests-for-phpunit.html#exceptions)
- [PHPUnit Documentation - Assertions](https://phpunit.readthedocs.io/en/9.2/assertions.html)

onelinerhub: [How to ignore warnings in PHPUnit?](https://onelinerhub.com/phpunit/how-to-ignore-warnings-in-phpunit)