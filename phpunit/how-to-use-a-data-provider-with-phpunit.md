# How to use a data provider with PHPUnit?
// plain

Using a data provider with PHPUnit is a great way to test a variety of inputs and outputs. It allows you to pass multiple arguments to a test method and run the same test multiple times with different data sets.

## Example code

```
<?php

class DataProviderTest extends \PHPUnit\Framework\TestCase
{
    /**
     * @dataProvider additionProvider
     */
    public function testAdd($a, $b, $expected)
    {
        $this->assertSame($expected, $a + $b);
    }

    public function additionProvider()
    {
        return [
            'adding zeros'  => [0, 0, 0],
            'zero plus one' => [0, 1, 1],
            'one plus zero' => [1, 0, 1],
            'one plus one'  => [1, 1, 3]
        ];
    }
}
```

## Output example

```
PHPUnit 8.5.8 by Sebastian Bergmann and contributors.

..                                                                  4 / 4 (100%)

Time: 00:00.001, Memory: 6.00 MB

OK (4 tests, 4 assertions)
```

## Code explanation


1. `class DataProviderTest extends \PHPUnit\Framework\TestCase` - This line declares the class that will contain the test method.

2. `@dataProvider additionProvider` - This annotation tells PHPUnit to use the `additionProvider` method as a data provider for the test method.

3. `public function testAdd($a, $b, $expected)` - This is the test method that will be run multiple times with different data sets.

4. `public function additionProvider()` - This is the data provider method that returns an array of data sets. Each data set is an array containing the arguments to be passed to the test method.

## Helpful links

- [PHPUnit Documentation - Data Providers](https://phpunit.readthedocs.io/en/9.2/writing-tests-for-phpunit.html#writing-tests-for-phpunit-data-providers)

onelinerhub: [How to use a data provider with PHPUnit?](https://onelinerhub.com/phpunit/how-to-use-a-data-provider-with-phpunit)