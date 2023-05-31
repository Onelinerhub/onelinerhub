# How to use a PHP function in Twig?
// plain

Twig is a templating language for PHP, and it's possible to use PHP functions in Twig. To do this, you need to register the function as a Twig extension.

## Example code

```
$twig = new Twig_Environment($loader);
$twig->addExtension(new Twig_Extension_StringLoader());
$twig->addFunction(new Twig_SimpleFunction('my_php_function', 'my_php_function'));
```

This code registers the `my_php_function` function as a Twig extension. Now you can use it in Twig templates like this:

```
{{ my_php_function('foo', 'bar') }}
```

## Code explanation


1. `$twig = new Twig_Environment($loader);` - creates a new Twig environment.
2. `$twig->addExtension(new Twig_Extension_StringLoader());` - adds the StringLoader extension to the Twig environment.
3. `$twig->addFunction(new Twig_SimpleFunction('my_php_function', 'my_php_function'));` - registers the `my_php_function` function as a Twig extension.
4. `{{ my_php_function('foo', 'bar') }}` - calls the `my_php_function` function in a Twig template.

## Helpful links

- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [Twig Extensions](https://twig.symfony.com/doc/2.x/advanced.html#creating-an-extension)

onelinerhub: [How to use a PHP function in Twig?](https://onelinerhub.com/twig/how-to-use-a-php-function-in-twig-)