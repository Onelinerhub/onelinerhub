# How to use the PHP Symfony form types?
// plain

The Symfony Form component provides a set of classes to help you build complex and maintainable forms. It allows you to create, process and reuse HTML forms.

To use the PHP Symfony form types, you need to create a form class and add the fields you want to use. For example:

```php
<?php

namespace App\Form;

use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\FormBuilderInterface;

class MyFormType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options)
    {
        $builder
            ->add('name')
            ->add('email')
            ->add('message', TextareaType::class)
        ;
    }
}
```

The code above creates a form with three fields: name, email and message.

To render the form in a template, you can use the `form_start()` and `form_end()` functions:

```twig
{{ form_start(form) }}
    {{ form_row(form.name) }}
    {{ form_row(form.email) }}
    {{ form_row(form.message) }}
    <button type="submit">Submit</button>
{{ form_end(form) }}
```

The output of the code above will be an HTML form with the three fields and a submit button.

## Helpful links

- [Symfony Form Component Documentation](https://symfony.com/doc/current/forms.html)
- [Twig Form Functions Documentation](https://twig.symfony.com/doc/3.x/forms.html)

onelinerhub: [How to use the PHP Symfony form types?](https://onelinerhub.com/php-symfony/how-to-use-the-php-symfony-form-types)