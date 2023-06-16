# How do I write and run tests in Laravel using PHP?
// plain

Writing and running tests in Laravel using PHP is quite easy. The following steps will guide you through the process:

1. Create a test class:

```php
<?php

use PHPUnit\Framework\TestCase;

class ExampleTest extends TestCase
{
    // test methods
}
```

2. Add test methods to the class:

```php
<?php

use PHPUnit\Framework\TestCase;

class ExampleTest extends TestCase
{
    public function testSomething()
    {
        $this->assertTrue(true);
    }
}
```

3. Run the tests using the `phpunit` command:

```
$ phpunit

PHPUnit 7.5.20 by Sebastian Bergmann and contributors.

..                                                                  2 / 2 (100%)

Time: 00:00.001, Memory: 6.00 MB

OK (2 tests, 2 assertions)
```

4. Assertions can be used to verify the expected outputs:

```php
<?php

use PHPUnit\Framework\TestCase;

class ExampleTest extends TestCase
{
    public function testSomething()
    {
        $this->assertEquals(2, 1 + 1);
    }
}
```

```
$ phpunit

PHPUnit 7.5.20 by Sebastian Bergmann and contributors.

.                                                                   1 / 1 (100%)

Time: 00:00.001, Memory: 6.00 MB

OK (1 test, 1 assertion)
```

For more information, please refer to the [Laravel documentation](https://laravel.com/docs/7.x/testing) and the [PHPUnit documentation](https://phpunit.readthedocs.io/en/latest/).

onelinerhub: [How do I write and run tests in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-write-and-run-tests-in-laravel-using-php)