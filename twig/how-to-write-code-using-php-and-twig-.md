# How to write code using PHP and Twig?
// plain

Writing code using PHP and Twig is a powerful combination for creating dynamic webpages. Twig is a templating language for PHP, and it allows you to write concise and readable code.

## Example code

```
<?php
$loader = new Twig_Loader_Filesystem('templates');
$twig = new Twig_Environment($loader);

echo $twig->render('index.html', array('name' => 'Fabien'));
```

## Output example

```
Hello Fabien
```

The code above loads the Twig environment, and renders the `index.html` template with the variable `name` set to `Fabien`.

The code consists of the following parts:

1. `$loader`: This is an instance of `Twig_Loader_Filesystem`, which is used to specify the directory where the templates are stored.
2. `$twig`: This is an instance of `Twig_Environment`, which is used to load the templates.
3. `render()`: This is a method of `Twig_Environment` which is used to render the template with the given variables.

For more information, please refer to the [Twig documentation](https://twig.symfony.com/doc/2.x/).

onelinerhub: [How to write code using PHP and Twig?](https://onelinerhub.com/twig/how-to-write-code-using-php-and-twig-)