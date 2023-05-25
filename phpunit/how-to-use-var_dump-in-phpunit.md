# How to use var_dump in PHPUnit?
// plain

Var_dump is a PHP function used to display structured information about variables and their content. It can be used in PHPUnit to display information about variables during the execution of a test.

## Example

```
<?php

class MyTest extends \PHPUnit\Framework\TestCase
{
    public function testVarDump()
    {
        $var = 'test';
        var_dump($var);
    }
}
```
## Output example

```
string(4) "test"
```

The code above shows how to use var_dump in a PHPUnit test. The code creates a variable called $var and assigns it the value 'test'. The var_dump function is then used to display the contents of the variable. The output of the code is 'string(4) "test"', which indicates that the variable is a string of length 4 containing the value 'test'.

## Helpful links

- [PHP: var_dump - Manual](https://www.php.net/manual/en/function.var-dump.php)
- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)