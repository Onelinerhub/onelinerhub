# Unit testing in PHP Symfony example
// plain

Unit testing is a process of testing individual units of code in order to ensure that they are working as expected. In PHP Symfony, unit testing is done using PHPUnit.

## Example code

```
<?php

namespace App\Tests;

use PHPUnit\Framework\TestCase;

class ExampleTest extends TestCase
{
    public function testExample()
    {
        $this->assertTrue(true);
    }
}
```

## Output example

```
OK (1 test, 1 assertion)
```

## Code explanation

- `namespace App\Tests;` - declares the namespace of the test class
- `use PHPUnit\Framework\TestCase;` - imports the TestCase class from the PHPUnit framework
- `class ExampleTest extends TestCase` - declares the test class which extends the TestCase class
- `public function testExample()` - declares the test method
- `$this->assertTrue(true);` - asserts that the given expression is true

## Helpful links
- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/9.2/)
- [Symfony Documentation - Testing](https://symfony.com/doc/current/testing.html)

onelinerhub: [Unit testing in PHP Symfony example](https://onelinerhub.com/php-symfony/unit-testing-in-php-symfony-example)