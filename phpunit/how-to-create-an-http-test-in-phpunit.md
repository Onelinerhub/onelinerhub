# How to create an HTTP test in PHPUnit?
// plain

Creating an HTTP test in PHPUnit is a simple process.

```
<?php

use PHPUnit\Framework\TestCase;

class HttpTest extends TestCase
{
    public function testHttp()
    {
        $this->assertTrue(true);
    }
}
```

This example code will output:

```
OK (1 test, 1 assertion)
```

## Code explanation


1. `use PHPUnit\Framework\TestCase;` - This imports the TestCase class from the PHPUnit framework.

2. `class HttpTest extends TestCase` - This creates a class called HttpTest which extends the TestCase class.

3. `public function testHttp()` - This creates a public function called testHttp which will contain the test code.

4. `$this->assertTrue(true);` - This is the actual test code which asserts that the given expression is true.

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)
- [PHPUnit Tutorial](https://phpunit.de/manual/current/en/writing-tests-for-phpunit.html)

onelinerhub: [How to create an HTTP test in PHPUnit?](https://onelinerhub.com/phpunit/how-to-create-an-http-test-in-phpunit)