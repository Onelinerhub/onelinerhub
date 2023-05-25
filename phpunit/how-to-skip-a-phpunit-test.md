# How to skip a PHPUnit test?
// plain

You can skip a PHPUnit test by using the `@doesNotPerformAssertions` annotation. This annotation will cause the test to be marked as skipped, and no assertions will be performed.

## Example

```
<?php

use PHPUnit\Framework\TestCase;

class MyTest extends TestCase
{
    /**
     * @doesNotPerformAssertions
     */
    public function testSomething()
    {
        // No assertions will be performed
    }
}
```

The `@doesNotPerformAssertions` annotation can be used to skip a test without having to comment out the test code.

## Code explanation


1. `@doesNotPerformAssertions` annotation - This annotation is used to mark the test as skipped, and no assertions will be performed.

2. Test code - The test code is the code that will be skipped.

## Helpful links

- [PHPUnit Documentation - Skipping Tests](https://phpunit.readthedocs.io/en/9.2/skipping-tests.html)

onelinerhub: [How to skip a PHPUnit test?](https://onelinerhub.com/phpunit/how-to-skip-a-phpunit-test)