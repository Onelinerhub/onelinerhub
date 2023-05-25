# How to ignore a test in PHPUnit?
// plain

To ignore a test in PHPUnit, you can use the `@test` annotation. This annotation can be used to mark a test as skipped, which will cause it to be ignored when running the test suite.

## Example

```
<?php

class MyTest extends \PHPUnit\Framework\TestCase
{
    /**
     * @test
     */
    public function testSomething()
    {
        // ...
    }

    /**
     * @test
     */
    public function testSomethingElse()
    {
        // ...
    }

    /**
     * @test
     * @ignore
     */
    public function testSomethingElse2()
    {
        // ...
    }
}
```

The `@test` annotation is used to mark a test as a test, and the `@ignore` annotation is used to mark a test as skipped. This will cause the test to be ignored when running the test suite.

## Code explanation

- `@test` annotation: marks a test as a test
- `@ignore` annotation: marks a test as skipped

## Helpful links
- [PHPUnit Documentation - Annotations](https://phpunit.readthedocs.io/en/9.2/annotations.html)

onelinerhub: [How to ignore a test in PHPUnit?](https://onelinerhub.com/phpunit/how-to-ignore-a-test-in-phpunit)