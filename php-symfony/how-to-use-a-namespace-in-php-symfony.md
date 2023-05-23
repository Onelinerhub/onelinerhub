# How to use a namespace in PHP Symfony?
// plain

Namespaces are used in PHP Symfony to organize classes and functions into logical groups. This helps to avoid name collisions between different classes and functions.

## Example code

```
namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;

class HelloController
{
    public function index()
    {
        return new Response('Hello World!');
    }
}
```

## Output example

```
Hello World!
```

## Code explanation

- `namespace App\Controller;` - This line declares the namespace of the class.
- `use Symfony\Component\HttpFoundation\Response;` - This line imports the Response class from the Symfony HttpFoundation component.
- `class HelloController` - This line declares the HelloController class.
- `public function index()` - This line declares the index() method of the HelloController class.
- `return new Response('Hello World!');` - This line returns a new Response object with the text "Hello World!"

## Helpful links
- [Namespaces in PHP](https://www.php.net/manual/en/language.namespaces.php)
- [Symfony HttpFoundation Component](https://symfony.com/doc/current/components/http_foundation.html)

onelinerhub: [How to use a namespace in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-a-namespace-in-php-symfony)