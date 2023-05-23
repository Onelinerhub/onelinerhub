# How to do validation in PHP Symfony?
// plain

Validation in PHP Symfony can be done using the Validator component. It provides a set of constraints which can be used to validate data.

## Example code

```
use Symfony\Component\Validator\Validation;
use Symfony\Component\Validator\Constraints\Length;

$validator = Validation::createValidator();
$violations = $validator->validate('abcde', [
    new Length(['min' => 3, 'max' => 5]),
]);

echo count($violations);
```

## Output example

```
0
```

## Code explanation

- `use Symfony\Component\Validator\Validation;` - imports the Validation class from the Validator component
- `use Symfony\Component\Validator\Constraints\Length;` - imports the Length constraint from the Validator component
- `$validator = Validation::createValidator();` - creates a validator instance
- `$violations = $validator->validate('abcde', [new Length(['min' => 3, 'max' => 5]),]);` - validates the string 'abcde' against the Length constraint with min and max values
- `echo count($violations);` - prints the number of violations

## Helpful links
- [Symfony Validator Component](https://symfony.com/doc/current/components/validator.html)
- [Validation Constraints](https://symfony.com/doc/current/validation.html#supported-constraints)

onelinerhub: [How to do validation in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-do-validation-in-php-symfony)