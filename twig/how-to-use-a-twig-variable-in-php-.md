# How to use a Twig variable in PHP?
// plain

Using a Twig variable in PHP is possible by using the `Twig_Environment` class. This class allows you to render a Twig template and get the output as a string.

```php
$loader = new Twig_Loader_Filesystem('/path/to/templates');
$twig = new Twig_Environment($loader);

$template = $twig->load('template.twig');
$output = $template->render(array('name' => 'Fabien'));
```

The output of the above code will be the rendered Twig template with the `name` variable replaced with `Fabien`.

## Code explanation


1. `Twig_Loader_Filesystem`: This class is used to specify the path to the Twig templates.
2. `Twig_Environment`: This class is used to create an instance of the Twig environment.
3. `$twig->load`: This method is used to load a Twig template.
4. `$template->render`: This method is used to render the Twig template and pass in any variables.
5. `$output`: This variable will contain the rendered Twig template.

## Helpful links

- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [Twig for Template Designers](https://twig.symfony.com/doc/2.x/templates.html)

onelinerhub: [How to use a Twig variable in PHP?](https://onelinerhub.com/twig/how-to-use-a-twig-variable-in-php-)