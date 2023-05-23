# How to use the PHP Symfony form?
// plain

The Symfony form component provides a set of classes to help you build complex, database-backed forms quickly and easily.

To use the Symfony form, you need to create a form class that extends the `AbstractType` class. This class will contain the form fields and their configuration.

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
            ->add('name', TextType::class)
            ->add('email', EmailType::class)
            ->add('save', SubmitType::class)
        ;
    }
}
```

The `buildForm` method is used to define the form fields and their configuration. In this example, we have added a `name` field of type `TextType`, an `email` field of type `EmailType`, and a `save` button of type `SubmitType`.

To render the form in a template, you can use the `form_start`, `form_row`, and `form_end` Twig functions:

```twig
{{ form_start(form) }}
    {{ form_row(form.name) }}
    {{ form_row(form.email) }}
    {{ form_row(form.save) }}
{{ form_end(form) }}
```

To process the form submission, you can use the `handleRequest` method of the form object:

```php
$form->handleRequest($request);

if ($form->isSubmitted() && $form->isValid()) {
    // ...
}
```

## Helpful links

- [Symfony Documentation - Forms](https://symfony.com/doc/current/forms.html)
- [Symfony Documentation - Form Types](https://symfony.com/doc/current/reference/forms/types.html)

onelinerhub: [How to use the PHP Symfony form?](https://onelinerhub.com/php-symfony/how-to-use-the-php-symfony-form)