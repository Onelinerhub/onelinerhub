# How to mock with PHPUnit?
// plain

PHPUnit provides a powerful mocking framework for testing code. It allows you to create mock objects that simulate the behavior of real objects.

## Example code

```
<?php

use PHPUnit\Framework\TestCase;

class MyTest extends TestCase
{
    public function testSomething()
    {
        // Create a mock object of the class we want to test
        $mock = $this->getMockBuilder('MyClass')
                     ->setMethods(['doSomething'])
                     ->getMock();

        // Configure the mock object
        $mock->expects($this->once())
             ->method('doSomething')
             ->will($this->returnValue('foo'));

        // Run the test
        $this->assertEquals('foo', $mock->doSomething());
    }
}
```

## Output example

```
OK (1 test, 1 assertion)
```

## Code explanation


1. `$mock = $this->getMockBuilder('MyClass')` - creates a mock object of the class we want to test.
2. `->setMethods(['doSomething'])` - sets the methods that should be mocked.
3. `->getMock()` - returns the mock object.
4. `$mock->expects($this->once())` - sets the expectation that the method `doSomething` should be called once.
5. `->method('doSomething')` - specifies the method to be mocked.
6. `->will($this->returnValue('foo'))` - sets the return value of the mocked method.
7. `$this->assertEquals('foo', $mock->doSomething())` - runs the test and checks that the return value of the mocked method is `foo`.

## Helpful links

- [PHPUnit Documentation - Mock Objects](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#mock-objects)
- [PHPUnit Documentation - Mock Builder](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#mock-builder)

onelinerhub: [How to mock with PHPUnit?](https://onelinerhub.com/phpunit/how-to-mock-with-phpunit)