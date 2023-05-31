# How to use a Twig file in PHP?
// plain

Twig is a templating language for PHP, which allows developers to write concise and readable code. It is used to separate the presentation layer from the application logic.

To use a Twig file in PHP, you need to include the Twig library in your project and create a Twig environment.

```php
// Include the Twig library
require_once 'vendor/autoload.php';

// Create a Twig environment
$loader = new \Twig\Loader\FilesystemLoader('templates');
$twig = new \Twig\Environment($loader);
```

The code above includes the Twig library and creates a Twig environment. The `FilesystemLoader` class is used to specify the directory where the Twig templates are stored.

To render a Twig template, you can use the `render()` method of the `Environment` class.

```php
// Render a Twig template
echo $twig->render('template.twig', ['name' => 'John']);
```

The code above renders the `template.twig` template and passes the `name` variable with the value `John` to the template.

## Helpful links

- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [Twig for Template Designers](https://twig.symfony.com/doc/2.x/templates.html)

onelinerhub: [How to use a Twig file in PHP?](https://onelinerhub.com/twig/how-to-use-a-twig-file-in-php-)