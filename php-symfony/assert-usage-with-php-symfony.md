# Assert usage with PHP Symfony
// plain

Assert is a PHP library that provides a set of assertion methods for validating the input of a Symfony application. It is part of the Symfony PHPUnit Bridge and is used to validate the input of a Symfony application.

## Example code

```
use Symfony\Component\Validator\Constraints as Assert;

class User
{
    /**
     * @Assert\NotBlank()
     */
    public $name;
}
```

The example code above uses the `@Assert\NotBlank()` annotation to validate that the `name` property of the `User` class is not blank.

## Code explanation

- `use Symfony\Component\Validator\Constraints as Assert;`: This imports the `Assert` namespace from the `Symfony\Component\Validator` namespace.
- `@Assert\NotBlank()`: This is an annotation that is used to validate that the `name` property of the `User` class is not blank.

## Helpful links
- [Assert Documentation](https://symfony.com/doc/current/components/validator.html#assert)
- [Symfony PHPUnit Bridge Documentation](https://symfony.com/doc/current/testing/phpunit_bridge.html)

onelinerhub: [Assert usage with PHP Symfony](https://onelinerhub.com/php-symfony/assert-usage-with-php-symfony)