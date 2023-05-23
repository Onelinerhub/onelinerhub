# How to use PHP Translation/Symfony Bundle?
// plain

PHP Translation/Symfony Bundle is a library that provides a set of tools for translating applications written in PHP. It is based on the Symfony Translation Component and provides a simple and powerful way to manage translations.

## Example code

```php
<?php

use Symfony\Component\Translation\Translator;

$translator = new Translator('en');
$translator->addLoader('array', new ArrayLoader());
$translator->addResource('array', array('hello' => 'Hello World!'), 'en');

echo $translator->trans('hello');
```

## Output example

```
Hello World!
```

## Code explanation

- `use Symfony\Component\Translation\Translator;` - This line imports the Translator class from the Symfony Translation Component.
- `$translator = new Translator('en');` - This line creates a new Translator instance with the language set to 'en'.
- `$translator->addLoader('array', new ArrayLoader());` - This line adds an ArrayLoader instance to the Translator instance. The ArrayLoader is used to load translation resources from an array.
- `$translator->addResource('array', array('hello' => 'Hello World!'), 'en');` - This line adds a translation resource to the Translator instance. The resource is an array containing a single translation with the key 'hello' and the value 'Hello World!'.
- `echo $translator->trans('hello');` - This line calls the trans() method on the Translator instance to translate the key 'hello'.

## Helpful links
- [Symfony Translation Component](https://symfony.com/doc/current/components/translation.html)
- [PHP Translation/Symfony Bundle](https://github.com/php-translation/symfony-bundle)

onelinerhub: [How to use PHP Translation/Symfony Bundle?](https://onelinerhub.com/php-symfony/how-to-use-php-translation-symfony-bundle)