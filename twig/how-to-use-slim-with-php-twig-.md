# How to use Slim with PHP Twig?
// plain

Slim is a PHP micro-framework that can be used with Twig, a template engine for PHP. To use Slim with Twig, you need to install the Slim-Views package.

```
composer require slim/slim-views
```

Once installed, you can configure Slim to use Twig as the default template engine.

```
$container['view'] = function ($container) {
    $view = new \Slim\Views\Twig(__DIR__ . '/../templates', [
        'cache' => false
    ]);

    // Instantiate and add Slim specific extension
    $basePath = rtrim(str_ireplace('index.php', '', $container['request']->getUri()->getBasePath()), '/');
    $view->addExtension(new Slim\Views\TwigExtension($container['router'], $basePath));

    return $view;
};
```

The code above configures Slim to use Twig as the default template engine. It also adds the Slim-specific Twig extension which allows you to use the `urlFor` function to generate URLs.

Parts of the code:

- `$container['view']`: This is the Slim container which holds the view configuration.
- `new \Slim\Views\Twig`: This instantiates a new Twig view.
- `$basePath`: This is the base path of the request.
- `$view->addExtension`: This adds the Slim-specific Twig extension.

## Helpful links

- [Slim Framework](https://www.slimframework.com/)
- [Twig Template Engine](https://twig.symfony.com/)
- [Slim-Views Package](https://github.com/slimphp/Slim-Views)

onelinerhub: [How to use Slim with PHP Twig?](https://onelinerhub.com/twig/how-to-use-slim-with-php-twig-)