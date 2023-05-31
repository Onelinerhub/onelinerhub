# How to render a Twig template from a string using PHP?
// plain

Rendering a Twig template from a string using PHP is possible with the help of the Twig_Loader_String class. This class allows you to load a template from a string instead of a file.

```php
// Create a Twig Loader
$loader = new Twig_Loader_String();

// Create a Twig Environment
$twig = new Twig_Environment($loader);

// Render a template
echo $twig->render('Hello {{ name }}!', array('name' => 'John Doe'));
```

## Output example

```
Hello John Doe!
```

## Code explanation

- `Twig_Loader_String`: This class allows you to load a template from a string instead of a file.
- `Twig_Environment`: This class is used to create a Twig Environment.
- `render`: This method is used to render a template.

## Helpful links
- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [Twig_Loader_String](https://twig.symfony.com/doc/2.x/api.html#twig-loader-string)

onelinerhub: [How to render a Twig template from a string using PHP?](https://onelinerhub.com/twig/how-to-render-a-twig-template-from-a-string-using-php-)