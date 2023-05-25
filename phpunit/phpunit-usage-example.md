# PHPUnit usage example
// plain

PHPUnit is a unit testing framework for the PHP language. It is used to test the functionality of individual units of code.

## Example


```
<?php

class MyTest extends PHPUnit_Framework_TestCase
{
    public function testAdd()
    {
        $this->assertEquals(4, 2 + 2);
    }
}
```

## Output example


```
OK (1 test, 1 assertion)
```

## Code explanation


1. `class MyTest extends PHPUnit_Framework_TestCase` - This line declares a class called MyTest which extends the PHPUnit_Framework_TestCase class.

2. `public function testAdd()` - This line declares a public function called testAdd.

3. `$this->assertEquals(4, 2 + 2)` - This line uses the assertEquals method to check if the result of 2 + 2 is equal to 4.

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)
- [PHPUnit Tutorial](https://phpunit.de/manual/current/en/index.html)

onelinerhub: [PHPUnit usage example](https://onelinerhub.com/phpunit/phpunit-usage-example)