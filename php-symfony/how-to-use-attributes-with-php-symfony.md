# How to use attributes with PHP Symfony?
// plain

Attributes are a powerful feature of PHP Symfony that allow developers to create reusable code.

## Example code

```
<?php

namespace App\Entity;

use Symfony\Component\Validator\Constraints as Assert;

class User
{
    /**
     * @Assert\NotBlank
     */
    private $name;
}
```

This code uses the `@Assert\NotBlank` attribute to ensure that the `name` property of the `User` class is not empty.

The code consists of the following parts:

1. `namespace App\Entity;` - This declares the namespace of the class.
2. `use Symfony\Component\Validator\Constraints as Assert;` - This imports the `Constraints` class from the `Symfony\Component\Validator` namespace and assigns it to the `Assert` alias.
3. `class User` - This declares the `User` class.
4. `@Assert\NotBlank` - This is the attribute that is applied to the `name` property. It ensures that the property is not empty.

## Helpful links

- [Symfony Documentation - Attributes](https://symfony.com/doc/current/components/validator/attributes.html)
- [Symfony Documentation - Validation](https://symfony.com/doc/current/validation.html)

onelinerhub: [How to use attributes with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-attributes-with-php-symfony)