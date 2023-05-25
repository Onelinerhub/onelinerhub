# How to use a listener with PHPUnit?
// plain

PHPUnit provides a listener interface which allows you to customize the behavior of the test suite. To use a listener with PHPUnit, you need to implement the `PHPUnit_Framework_TestListener` interface.

## Example code

```php
<?php

use PHPUnit\Framework\TestListener;

class MyListener implements TestListener
{
    public function startTestSuite(PHPUnit_Framework_TestSuite $suite)
    {
        // Do something before the test suite starts
    }

    public function endTestSuite(PHPUnit_Framework_TestSuite $suite)
    {
        // Do something after the test suite ends
    }
}
```

The example code above implements a listener that will execute code before and after the test suite starts and ends.

To use the listener, you need to register it with the test suite. This can be done by passing an instance of the listener to the `addListener()` method of the `PHPUnit_Framework_TestSuite` class.

## Example code

```php
<?php

$suite = new PHPUnit_Framework_TestSuite();
$listener = new MyListener();
$suite->addListener($listener);
```

The example code above registers the `MyListener` instance with the test suite.

## Helpful links

- [PHPUnit Documentation - Test Listeners](https://phpunit.readthedocs.io/en/latest/writing-tests-for-phpunit.html#test-listeners)

onelinerhub: [How to use a listener with PHPUnit?](https://onelinerhub.com/phpunit/how-to-use-a-listener-with-phpunit)