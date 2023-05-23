# How to use PHP Symfony components?
// plain

PHP Symfony components are a set of decoupled and reusable PHP libraries. They can be used to develop web applications and speed up development process.

## Example code

```
<?php

require_once __DIR__.'/vendor/autoload.php';

use Symfony\Component\HttpFoundation\Request;

$request = Request::createFromGlobals();

echo $request->getPathInfo();
```

## Output example

```
/
```

## Code explanation

- `require_once __DIR__.'/vendor/autoload.php';` - this line includes the autoloader file which is responsible for loading all the necessary components.
- `use Symfony\Component\HttpFoundation\Request;` - this line imports the Request class from the Symfony HttpFoundation component.
- `$request = Request::createFromGlobals();` - this line creates a Request object from the global variables.
- `echo $request->getPathInfo();` - this line prints the path info of the request.

## Helpful links
- [Symfony Components](https://symfony.com/components)
- [HttpFoundation Component](https://symfony.com/doc/current/components/http_foundation.html)

onelinerhub: [How to use PHP Symfony components?](https://onelinerhub.com/php-symfony/how-to-use-php-symfony-components)