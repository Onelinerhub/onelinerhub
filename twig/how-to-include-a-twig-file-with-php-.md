# How to include a Twig file with PHP?
// plain

Twig is a templating language for PHP. It can be used to include a Twig file with PHP by using the `Twig_Environment` class.

## Example code

```
<?php
$loader = new Twig_Loader_Filesystem('templates');
$twig = new Twig_Environment($loader);
echo $twig->render('template.twig');
```

## Output example

```
<html>
  <head>
    <title>My Webpage</title>
  </head>
  <body>
    <h1>Welcome to my Webpage!</h1>
  </body>
</html>
```

## Code explanation

- `Twig_Loader_Filesystem('templates')`: This creates a new Twig_Loader_Filesystem object, which is used to locate the Twig template files.
- `Twig_Environment($loader)`: This creates a new Twig_Environment object, which is used to render the Twig template.
- `render('template.twig')`: This renders the Twig template file `template.twig` and returns the output as a string.

## Helpful links
- [Twig Documentation](https://twig.symfony.com/doc/2.x/)

onelinerhub: [How to include a Twig file with PHP?](https://onelinerhub.com/twig/how-to-include-a-twig-file-with-php-)