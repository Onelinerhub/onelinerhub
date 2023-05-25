# How to use named arguments in PHPUnit?
// plain

Named arguments are used to pass parameters to a function in PHPUnit. They are used to make the code more readable and easier to maintain.

## Example

```
<?php

class MyTest extends \PHPUnit\Framework\TestCase
{
    public function testNamedArguments()
    {
        $this->assertEquals(
            'Hello World',
            myFunction('Hello', 'World')
        );
    }
}

function myFunction($first, $second)
{
    return $first . ' ' . $second;
}
```

## Output example

```
Hello World
```

## Code explanation


1. `$this->assertEquals('Hello World', myFunction('Hello', 'World'));` - This line is used to call the `myFunction` function with two named arguments, `'Hello'` and `'World'`.

2. `function myFunction($first, $second)` - This line is used to define the `myFunction` function with two parameters, `$first` and `$second`.

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)

onelinerhub: [How to use named arguments in PHPUnit?](https://onelinerhub.com/phpunit/how-to-use-named-arguments-in-phpunit)