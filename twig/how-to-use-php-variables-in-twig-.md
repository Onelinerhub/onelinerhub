# How to use PHP variables in Twig?
// plain

Twig is a templating language for PHP, and it allows you to use PHP variables in your Twig templates. To do this, you need to pass the variables to the Twig environment when you create it.

```php
$loader = new Twig_Loader_Filesystem('templates');
$twig = new Twig_Environment($loader);

$name = 'John';
$twig->addGlobal('name', $name);
```

The above code creates a Twig environment and adds a global variable `name` with the value `John`. This variable can now be used in any Twig template.

```
Hello {{ name }}
```

## Output example

```
Hello John
```

## Code explanation


1. `$loader = new Twig_Loader_Filesystem('templates');` - creates a Twig loader object which is used to load Twig templates.
2. `$twig = new Twig_Environment($loader);` - creates a Twig environment object which is used to render Twig templates.
3. `$name = 'John';` - creates a PHP variable with the value `John`.
4. `$twig->addGlobal('name', $name);` - adds the PHP variable `name` to the Twig environment as a global variable.
5. `Hello {{ name }}` - uses the global variable `name` in a Twig template.

## Helpful links

- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [Twig for Template Designers](https://twig.symfony.com/doc/2.x/templates.html)

onelinerhub: [How to use PHP variables in Twig?](https://onelinerhub.com/twig/how-to-use-php-variables-in-twig-)