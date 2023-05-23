# How to use the validator in PHP Symfony?
// plain

The Validator component in PHP Symfony is used to validate data. It can be used to validate data from forms, databases, and any other source.

## Example code

```
use Symfony\Component\Validator\Validation;

$validator = Validation::createValidator();
$violations = $validator->validate('Bernhard', array(
    new NotBlank(),
    new Length(array('min' => 10)),
));

if (0 !== count($violations)) {
    // there are errors, now you can show them
    foreach ($violations as $violation) {
        echo $violation->getMessage().'<br>';
    }
}
```

## Output example

```
This value is too short. It should have 10 characters or more.
```

## Code explanation


1. `use Symfony\Component\Validator\Validation;` - This line imports the Validation class from the Symfony Validator component.

2. `$validator = Validation::createValidator();` - This line creates a validator object.

3. `$violations = $validator->validate('Bernhard', array(
    new NotBlank(),
    new Length(array('min' => 10)),
));` - This line validates the string 'Bernhard' against the NotBlank and Length constraints.

4. `if (0 !== count($violations)) {` - This line checks if there are any violations.

5. `foreach ($violations as $violation) {
    echo $violation->getMessage().'<br>';
}` - This loop prints out the violation messages.

## Helpful links

- [Symfony Validator Component Documentation](https://symfony.com/doc/current/components/validator.html)
- [Validator Constraints Documentation](https://symfony.com/doc/current/validation.html#constraints)

onelinerhub: [How to use the validator in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-the-validator-in-php-symfony)