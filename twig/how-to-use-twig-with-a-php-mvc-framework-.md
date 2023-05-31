# How to use Twig with a PHP MVC framework?
// plain

Twig is a templating engine for PHP that can be used with a PHP MVC framework. It allows developers to write concise, readable code that is easy to maintain.

```
<?php
$loader = new Twig_Loader_Filesystem('templates');
$twig = new Twig_Environment($loader);

echo $twig->render('index.html', array('name' => 'Fabien'));
```

This example code will render the `index.html` template located in the `templates` directory, and pass the variable `name` with the value `Fabien` to the template.

Parts of the code:

- `Twig_Loader_Filesystem('templates')`: Loads the `templates` directory as the Twig template directory.
- `Twig_Environment($loader)`: Creates a new Twig environment with the given loader.
- `render('index.html', array('name' => 'Fabien'))`: Renders the `index.html` template with the given variables.

## Helpful links

- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [Twig for Template Designers](https://twig.symfony.com/doc/2.x/templates.html)

onelinerhub: [How to use Twig with a PHP MVC framework?](https://onelinerhub.com/twig/how-to-use-twig-with-a-php-mvc-framework-)