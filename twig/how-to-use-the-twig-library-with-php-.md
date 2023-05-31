# How to use the Twig library with PHP?
// plain

Twig is a templating library for PHP that allows developers to write concise, secure, and easy-to-maintain code. It is a fast and secure template engine for PHP.

To use Twig with PHP, first install the Twig library using Composer:

```
composer require "twig/twig:^2.0"
```

Then, create a Twig environment object and set the template directory:

```php
$loader = new \Twig\Loader\FilesystemLoader('templates');
$twig = new \Twig\Environment($loader);
```

Finally, render the template with the data:

```php
echo $twig->render('template.html', ['name' => 'John Doe']);
```

The code above will render the `template.html` file located in the `templates` directory, passing the `name` variable with the value `John Doe`.

For more information, please refer to the [Twig documentation](https://twig.symfony.com/doc/2.x/).

onelinerhub: [How to use the Twig library with PHP?](https://onelinerhub.com/twig/how-to-use-the-twig-library-with-php-)