# How to do testing with PHP Symfony?
// plain

Testing with PHP Symfony is a great way to ensure that your application is working as expected.

To get started, you can use the Symfony PHPUnit Bridge to integrate PHPUnit into your Symfony application.

```
composer require --dev symfony/phpunit-bridge
```

Once installed, you can create a test class in the `tests` directory of your application.

```
<?php

namespace App\Tests;

use PHPUnit\Framework\TestCase;

class ExampleTest extends TestCase
{
    public function testSomething()
    {
        $this->assertTrue(true);
    }
}
```

You can then run the tests with the `bin/phpunit` command.

```
$ bin/phpunit

PHPUnit 8.5.8 by Sebastian Bergmann and contributors.

..                                                                  2 / 2 (100%)

Time: 00:00.001, Memory: 6.00 MB

OK (2 tests, 2 assertions)
```

You can also use the Symfony Test Client to simulate HTTP requests and test the response.

## Helpful links

- [Symfony PHPUnit Bridge](https://symfony.com/doc/current/testing/phpunit_bridge.html)
- [Symfony Test Client](https://symfony.com/doc/current/testing/http_client.html)

onelinerhub: [How to do testing with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-do-testing-with-php-symfony)