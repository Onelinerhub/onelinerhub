# How to test an abstract class with PHPUnit?
// plain

Abstract classes can be tested with PHPUnit by creating a concrete subclass of the abstract class and then testing the subclass.

```
<?php

abstract class AbstractClass
{
    abstract protected function getValue();
    abstract protected function prefixValue($prefix);

    public function printOut()
    {
        print $this->getValue() . "\n";
    }
}

class ConcreteClass extends AbstractClass
{
    protected function getValue()
    {
        return "ConcreteClass";
    }

    public function prefixValue($prefix)
    {
        return "{$prefix}ConcreteClass";
    }
}

class AbstractClassTest extends PHPUnit_Framework_TestCase
{
    public function testGetValue()
    {
        $class = new ConcreteClass;
        $this->assertEquals('ConcreteClass', $class->getValue());
    }

    public function testPrefixValue()
    {
        $class = new ConcreteClass;
        $this->assertEquals('prefixedConcreteClass', $class->prefixValue('prefixed'));
    }
}
```

## Output example

```
PHPUnit 5.7.21 by Sebastian Bergmann and contributors.

..                                                                  2 / 2 (100%)

Time: 5 ms, Memory: 4.00MB

OK (2 tests, 2 assertions)
```

## Code explanation


1. `abstract class AbstractClass`: This is the abstract class that will be tested.
2. `class ConcreteClass extends AbstractClass`: This is the concrete subclass of the abstract class that will be tested.
3. `class AbstractClassTest extends PHPUnit_Framework_TestCase`: This is the test class that will be used to test the abstract class.
4. `public function testGetValue()`: This is a test method that tests the `getValue()` method of the abstract class.
5. `public function testPrefixValue()`: This is a test method that tests the `prefixValue()` method of the abstract class.

## Helpful links

1. [PHPUnit Documentation](https://phpunit.readthedocs.io/en/7.4/)
2. [Testing Abstract Classes with PHPUnit](https://phpunit.readthedocs.io/en/7.4/test-doubles.html#testing-abstract-classes)