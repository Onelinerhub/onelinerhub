# How to create a Twig template from a string using PHP?
// plain

Creating a Twig template from a string using PHP is a simple process. The following example code block shows how to do this:
```
$loader = new \Twig\Loader\ArrayLoader([
    'index' => 'Hello {{ name }}!',
]);
$twig = new \Twig\Environment($loader);

echo $twig->render('index', ['name' => 'Fabien']);
```
The output of this code is:
```
Hello Fabien!
```
The code consists of the following parts:

1. `$loader`: This is an instance of the `ArrayLoader` class, which is used to load templates from an array.
2. `$twig`: This is an instance of the `Environment` class, which is used to manage the Twig environment.
3. `render()`: This is a method of the `Environment` class, which is used to render a template.

For more information, please refer to the [Twig documentation](https://twig.symfony.com/doc/2.x/).

onelinerhub: [How to create a Twig template from a string using PHP?](https://onelinerhub.com/twig/how-to-create-a-twig-template-from-a-string-using-php-)