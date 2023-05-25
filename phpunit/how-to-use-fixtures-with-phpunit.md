# How to use fixtures with PHPUnit?
// plain

Fixtures are used to provide a known set of data to test against. PHPUnit provides a `DataProvider` annotation to allow for the creation of fixtures.

## Example code

```php
<?php

use PHPUnit\Framework\TestCase;

class MyTest extends TestCase
{
    /**
     * @dataProvider fixtureProvider
     */
    public function testFixture($fixture)
    {
        // Test code here
    }

    public function fixtureProvider()
    {
        return [
            [1],
            [2],
            [3],
        ];
    }
}
```

## Output example

```
PHPUnit 8.5.8 by Sebastian Bergmann and contributors.

.                                                                   3 / 3 (100%)

Time: 00:00.001, Memory: 6.00 MB

OK (3 tests, 3 assertions)
```

The `DataProvider` annotation is used to specify a method that will provide the data for the test. The method should return an array of arrays, with each inner array containing the data for a single test.

The example code creates a test class with a `testFixture` method that is annotated with the `@dataProvider` annotation. The `fixtureProvider` method is used to provide the data for the test. The `fixtureProvider` method returns an array of arrays, each containing a single value.

## Helpful links

- [PHPUnit Documentation - Data Providers](https://phpunit.readthedocs.io/en/9.2/writing-tests-for-phpunit.html#writing-tests-for-phpunit-data-providers)

onelinerhub: [How to use fixtures with PHPUnit?](https://onelinerhub.com/phpunit/how-to-use-fixtures-with-phpunit)