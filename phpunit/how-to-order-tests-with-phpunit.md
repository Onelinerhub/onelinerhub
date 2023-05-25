# How to order tests with PHPUnit?
// plain

PHPUnit provides a way to order tests using the `@depends` annotation. This annotation allows you to specify that a test method depends on another test method. The dependent test method will be run before the test method that depends on it.

For example:
```php
class MyTest extends TestCase
{
    public function testA()
    {
        // ...
    }

    /**
     * @depends testA
     */
    public function testB()
    {
        // ...
    }
}
```

The `@depends` annotation can also be used to specify multiple test methods that the current test method depends on.

For example:
```php
class MyTest extends TestCase
{
    public function testA()
    {
        // ...
    }

    public function testB()
    {
        // ...
    }

    /**
     * @depends testA
     * @depends testB
     */
    public function testC()
    {
        // ...
    }
}
```

In this example, `testC` will be run after both `testA` and `testB` have been run.

## Helpful links
- [PHPUnit Documentation - Test Dependencies](https://phpunit.readthedocs.io/en/9.2/writing-tests-for-phpunit.html#test-dependencies)

onelinerhub: [How to order tests with PHPUnit?](https://onelinerhub.com/phpunit/how-to-order-tests-with-phpunit)