# How to use PHPUnit before test hook?
// plain

PHPUnit is a popular unit testing framework for PHP. It can be used to test the functionality of a codebase before committing changes.

To use PHPUnit before a test hook, you need to install the PHPUnit library and create a test class.

```
// Install PHPUnit
composer require --dev phpunit/phpunit

// Create a test class
<?php

use PHPUnit\Framework\TestCase;

class MyTest extends TestCase
{
    public function testSomething()
    {
        // Test code goes here
    }
}
```

Then, you can run the test class with the `phpunit` command.

```
phpunit MyTest.php
```

The output of the command will show the results of the tests.

```
PHPUnit 8.5.2 by Sebastian Bergmann and contributors.

..                                                                  2 / 2 (100%)

Time: 00:00.001, Memory: 6.00 MB

OK (2 tests, 2 assertions)
```

## Code explanation


1. Install PHPUnit: `composer require --dev phpunit/phpunit`
2. Create a test class: `<?php use PHPUnit\Framework\TestCase; class MyTest extends TestCase { public function testSomething() { // Test code goes here } }`
3. Run the test class: `phpunit MyTest.php`

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)
- [Getting Started with PHPUnit](https://phpunit.readthedocs.io/en/latest/getting-started.html)

onelinerhub: [How to use PHPUnit before test hook?](https://onelinerhub.com/phpunit/how-to-use-phpunit-before-test-hook)