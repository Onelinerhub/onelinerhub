# How to use PHPUnit assert to check void?
// plain

PHPUnit provides an `assertNull()` method to check if a value is `null`. This method can be used to check if a void method returns `null`.

```
<?php

class MyClass
{
    public function voidMethod()
    {
        // do something
    }
}

$myClass = new MyClass();

$this->assertNull($myClass->voidMethod());
```

The code above will check if the `voidMethod()` returns `null`.

1. `$myClass = new MyClass();` - creates an instance of the `MyClass` class.
2. `$this->assertNull($myClass->voidMethod());` - calls the `assertNull()` method to check if the `voidMethod()` returns `null`.

## Helpful links

- [PHPUnit Documentation - Assertions](https://phpunit.readthedocs.io/en/9.2/assertions.html)
- [PHPUnit Documentation - assertNull()](https://phpunit.readthedocs.io/en/9.2/assertions.html#assertnull)

onelinerhub: [How to use PHPUnit assert to check void?](https://onelinerhub.com/phpunit/how-to-use-phpunit-assert-to-check-void)