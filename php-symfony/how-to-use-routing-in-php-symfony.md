# How to use Routing in PHP Symfony?
// plain

Routing in PHP Symfony is a way to map URLs to specific controller actions. It is done by creating a routing configuration file, which is usually stored in the `config/routes.yaml` file.

## Example code

```
# config/routes.yaml
blog_show:
    path: /blog/{slug}
    controller: App\Controller\BlogController::show
```

This example code will map the URL `/blog/{slug}` to the `show` action of the `BlogController` class. The `{slug}` part of the URL will be passed as an argument to the `show` action.

## Code explanation


1. `blog_show` - This is the name of the route.
2. `path` - This is the URL pattern that will be matched.
3. `controller` - This is the controller action that will be executed when the URL is matched.

## Helpful links

- [Routing in Symfony](https://symfony.com/doc/current/routing.html)
- [Routing Configuration](https://symfony.com/doc/current/routing/configuration.html)

onelinerhub: [How to use Routing in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-routing-in-php-symfony)