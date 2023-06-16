# How do I write a unit test in Laravel using PHP?
// plain

Unit testing in Laravel with PHP is done using the PHPUnit testing framework. The first step is to install the package with the command `composer require --dev phpunit/phpunit`.

Once installed, you can create a new test class by running the command `php artisan make:test MyTest`. This will create a new test class in the `tests/Unit` directory.

In the newly created test class, you can define the tests that you want to run. For example, the following test will check if the `add` method of the `Calculator` class returns the correct result:
```
<?php

namespace Tests\Unit;

use Tests\TestCase;
use App\Calculator;

class CalculatorTest extends TestCase
{
    public function testAdd()
    {
        $calculator = new Calculator;
        $this->assertEquals(30, $calculator->add(10, 20));
    }
}
```

The test can then be run from the command line using `phpunit`. Upon successful completion, you should see the following output:
```
PHPUnit 7.5.20 by Sebastian Bergmann and contributors.

.                                                                   1 / 1 (100%)

Time: 00:00.006, Memory: 6.00 MB

OK (1 test, 1 assertion)
```

The code above consists of the following parts:
* `namespace Tests\Unit` - defines the namespace of the test class
* `use Tests\TestCase` - imports the TestCase class which provides the necessary setup for the test
* `use App\Calculator` - imports the Calculator class which is being tested
* `public function testAdd()` - defines a test method which checks if the `add` method of the `Calculator` class returns the correct result
* `$calculator = new Calculator` - creates a new instance of the `Calculator` class
* `$this->assertEquals(30, $calculator->add(10, 20))` - checks if the result of the `add` method is equal to 30

For more information, see the [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/) and the [Laravel Documentation](https://laravel.com/docs/5.8/testing).

onelinerhub: [How do I write a unit test in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-write-a-unit-test-in-laravel-using-php)