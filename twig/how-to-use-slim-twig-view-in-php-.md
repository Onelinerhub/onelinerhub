# How to use Slim/Twig-View in PHP?
// plain

Slim/Twig-View is a combination of the Slim PHP micro-framework and the Twig templating engine. It allows developers to quickly create web applications with a powerful and flexible templating system.

## Example code

```
<?php
require 'vendor/autoload.php';

$app = new \Slim\Slim(array(
    'view' => new \Slim\Views\Twig()
));

$app->get('/hello/:name', function ($name) use ($app) {
    $app->render('hello.html', array(
        'name' => $name
    ));
});

$app->run();
```

## Output example

```
Hello, [name]!
```

The code above creates a Slim application with Twig-View as the view engine. The `$app->render()` method is used to render the `hello.html` template with the `name` variable. The template will output `Hello, [name]!` when rendered.

## Helpful links

- [Slim Framework](http://www.slimframework.com/)
- [Twig Templating Engine](http://twig.sensiolabs.org/)
- [Slim/Twig-View](https://github.com/codeguy/Slim-Views)

onelinerhub: [How to use Slim/Twig-View in PHP?](https://onelinerhub.com/twig/how-to-use-slim-twig-view-in-php-)