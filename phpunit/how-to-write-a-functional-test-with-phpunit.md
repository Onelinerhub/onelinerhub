# How to write a functional test with PHPUnit?
// plain

PHPUnit is a popular unit testing framework for PHP. It can be used to write functional tests for web applications.

To write a functional test with PHPUnit, you need to create a test class that extends the PHPUnit_Framework_TestCase class.

```
<?php
class MyFunctionalTest extends PHPUnit_Framework_TestCase
{
    public function testMyFunction()
    {
        // Test code goes here
    }
}
```

The test class should contain one or more test methods, which are the actual tests. Each test method should contain the code to test the functionality of the application.

- `MyFunctionalTest`: The test class that extends the `PHPUnit_Framework_TestCase` class.
- `testMyFunction()`: The test method that contains the code to test the functionality of the application.

For more information, please refer to the [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/).

onelinerhub: [How to write a functional test with PHPUnit?](https://onelinerhub.com/phpunit/how-to-write-a-functional-test-with-phpunit)