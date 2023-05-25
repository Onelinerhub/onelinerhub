# How to test protected methods in PHPUnit?
// plain

Testing protected methods in PHPUnit can be done using the `setAccessible()` method. This method allows us to access and test protected methods.

## Example

```
class MyClass {
    protected function myProtectedMethod() {
        return 'protected';
    }
}

$class = new MyClass;
$method = new ReflectionMethod($class, 'myProtectedMethod');
$method->setAccessible(true);
echo $method->invoke($class);
```
## Output example

```
protected
```

The code above consists of the following parts:

1. `class MyClass` - This is the class that contains the protected method.
2. `protected function myProtectedMethod()` - This is the protected method that we want to test.
3. `$class = new MyClass` - This creates an instance of the class.
4. `$method = new ReflectionMethod($class, 'myProtectedMethod')` - This creates a ReflectionMethod object for the protected method.
5. `$method->setAccessible(true)` - This sets the protected method to be accessible.
6. `echo $method->invoke($class)` - This invokes the protected method and prints the result.

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/9.2/)
- [ReflectionMethod Documentation](https://www.php.net/manual/en/class.reflectionmethod.php)

onelinerhub: [How to test protected methods in PHPUnit?](https://onelinerhub.com/phpunit/how-to-test-protected-methods-in-phpunit)