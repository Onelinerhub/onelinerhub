# How to use the PHPUnit Framework ExceptionWrapper?
// plain

PHPUnit Framework ExceptionWrapper is a utility class that helps to wrap exceptions thrown by the code under test. It provides a convenient way to catch and verify exceptions.

## Example code

```
try {
    // code that throws an exception
} catch (Exception $e) {
    $wrapper = new PHPUnit_Framework_ExceptionWrapper($e);
    // do something with the wrapper
}
```

The code above will catch any exception thrown by the code under test and wrap it in a PHPUnit_Framework_ExceptionWrapper object. This object can then be used to verify the exception, for example:

```
$this->assertEquals('My expected exception message', $wrapper->getMessage());
```

The PHPUnit_Framework_ExceptionWrapper class provides the following methods:

- getMessage(): Returns the exception message
- getCode(): Returns the exception code
- getFile(): Returns the file name where the exception was thrown
- getLine(): Returns the line number where the exception was thrown
- getTrace(): Returns the stack trace
- getPrevious(): Returns the previous exception

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)
- [PHPUnit ExceptionWrapper Class](https://phpunit.readthedocs.io/en/latest/api/PHPUnit_Framework_ExceptionWrapper.html)

onelinerhub: [How to use the PHPUnit Framework ExceptionWrapper?](https://onelinerhub.com/phpunit/how-to-use-the-phpunit-framework-exceptionwrapper)