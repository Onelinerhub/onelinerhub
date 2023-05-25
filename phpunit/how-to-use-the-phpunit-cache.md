# How to use the PHPUnit cache?
// plain

PHPUnit cache is a feature that allows you to store the results of a test run in a cache file. This can be used to speed up the execution of tests, as the results of the tests do not need to be re-run.

## Example code

```
<?php
use PHPUnit\Framework\TestCase;

class MyTest extends TestCase
{
    public function testSomething()
    {
        // ...
    }
}
```

To enable the cache, you need to add the following line to your phpunit.xml configuration file:

```
<phpunit cacheResult="true" cacheResultFile="my_test_cache.txt" />
```

The `cacheResult` attribute enables the cache, and the `cacheResultFile` attribute specifies the name of the cache file.

The cache file will be created in the same directory as the phpunit.xml file.

## Helpful links

- [PHPUnit Documentation - Caching Test Results](https://phpunit.readthedocs.io/en/9.2/fixtures.html#caching-test-results)

onelinerhub: [How to use the PHPUnit cache?](https://onelinerhub.com/phpunit/how-to-use-the-phpunit-cache)