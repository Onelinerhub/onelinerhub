# How to map a PHP array to Twig?
// plain

Mapping a PHP array to Twig is a simple process. You can use the `Twig_Environment` class to create a Twig environment and then use the `render` method to render a template with the array data.

```php
$loader = new Twig_Loader_Filesystem('templates');
$twig = new Twig_Environment($loader);

$data = array('name' => 'John', 'age' => 25);

echo $twig->render('template.twig', $data);
```

The output of the above code will be the rendered template with the data from the array.

## Code explanation


1. `Twig_Loader_Filesystem` - This class is used to load the template files.
2. `Twig_Environment` - This class is used to create a Twig environment.
3. `render` - This method is used to render a template with the array data.
4. `$data` - This is the array containing the data to be used in the template.

## Helpful links

- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [Twig for Template Designers](https://twig.symfony.com/doc/2.x/templates.html)

onelinerhub: [How to map a PHP array to Twig?](https://onelinerhub.com/twig/how-to-map-a-php-array-to-twig-)