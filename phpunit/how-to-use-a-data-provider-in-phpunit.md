# How to use a data provider in PHPUnit?
// plain

Data providers are a powerful feature of PHPUnit that allow you to pass multiple sets of data to a test method.

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
            'one plus one'  => [1, 1, 2]
        ];
    }
}
```

The output of the example code is:

```
OK (4 tests, 4 assertions)
```

## Code explanation


1. `@dataProvider additionProvider` - This annotation tells PHPUnit to use the `additionProvider` method as a data provider for the test method.
2. `public function additionProvider()` - This method returns an array of data sets to be used in the test method.
3. `$this->assertSame($expected, $a + $b);` - This assertion checks that the expected result matches the actual result of the addition.

## Helpful links

- [PHPUnit Data Providers](https://phpunit.readthedocs.io/en/9.2/writing-tests-for-phpunit.html#data-providers)

onelinerhub: [How to use a data provider in PHPUnit?](https://onelinerhub.com/phpunit/how-to-use-a-data-provider-in-phpunit)