# How to group tests in PHPUnit?
// plain

PHPUnit provides a way to group tests into logical units. This can be done by using the `@group` annotation. Tests can be grouped by feature, type, or any other criteria.

```php
<?php

use PHPUnit\Framework\TestCase;

class MyTest extends TestCase
{
    /**
     * @group feature
     */
    public function testFeatureA()
    {
        // ...
    }

    /**
     * @group feature
     */
    public function testFeatureB()
    {
        // ...
    }

    /**
     * @group type
     */
    public function testTypeA()
    {
        // ...
    }
}
```

The `@group` annotation can be used to group tests together. Tests can be grouped by feature, type, or any other criteria. Tests can then be run by group using the `--group` option.

```
$ phpunit --group feature
```

The code above will run all tests with the `@group feature` annotation.

## Helpful links

- [PHPUnit Documentation - Group Tests](https://phpunit.readthedocs.io/en/9.2/writing-tests-for-phpunit.html#grouping-tests)

onelinerhub: [How to group tests in PHPUnit?](https://onelinerhub.com/phpunit/how-to-group-tests-in-phpunit)