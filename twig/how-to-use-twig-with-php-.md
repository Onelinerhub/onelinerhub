# How to use Twig with PHP?
// plain

Twig is a templating engine for PHP. It allows developers to write HTML templates with a simple syntax that is easy to read and maintain.

```
<?php
require_once 'vendor/autoload.php';

$loader = new Twig_Loader_Filesystem('templates');
$twig = new Twig_Environment($loader);

echo $twig->render('index.html', array('name' => 'Fabien'));
```

This example code will render the `index.html` template located in the `templates` directory, and pass the `name` variable with the value `Fabien` to the template.

## Code explanation


1. `require_once 'vendor/autoload.php';` - This line loads the Twig autoloader, which is necessary for Twig to work.
2. `$loader = new Twig_Loader_Filesystem('templates');` - This line creates a new Twig loader object, which is used to locate the template files.
3. `$twig = new Twig_Environment($loader);` - This line creates a new Twig environment object, which is used to render the templates.
4. `echo $twig->render('index.html', array('name' => 'Fabien'));` - This line renders the `index.html` template, and passes the `name` variable with the value `Fabien` to the template.

## Helpful links

- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [Twig for Template Designers](https://twig.symfony.com/doc/2.x/templates.html)

onelinerhub: [How to use Twig with PHP?](https://onelinerhub.com/twig/how-to-use-twig-with-php-)