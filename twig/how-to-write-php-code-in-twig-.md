# How to write PHP code in Twig?
// plain

It is not possible to write PHP code directly in Twig. However, it is possible to call PHP functions from Twig templates. To do this, you need to create a custom Twig extension and register it with the Twig environment.

Example code block:
```php
<?php

use Twig\Extension\AbstractExtension;

class MyTwigExtension extends AbstractExtension
{
    public function getFunctions()
    {
        return [
            new \Twig\TwigFunction('my_php_function', [$this, 'myPhpFunction']),
        ];
    }

    public function myPhpFunction()
    {
        return 'Hello from PHP!';
    }
}
```

Output of example code:
```
Hello from PHP!
```

## Code explanation


1. `use Twig\Extension\AbstractExtension;` - This line imports the AbstractExtension class from the Twig namespace.

2. `class MyTwigExtension extends AbstractExtension` - This line creates a new class called MyTwigExtension which extends the AbstractExtension class.

3. `public function getFunctions()` - This is a method which returns an array of Twig functions.

4. `new \Twig\TwigFunction('my_php_function', [$this, 'myPhpFunction'])` - This line creates a new Twig function called my_php_function which calls the myPhpFunction() method.

5. `public function myPhpFunction()` - This is the method which is called by the my_php_function Twig function.

6. `return 'Hello from PHP!';` - This line returns a string which is the output of the my_php_function Twig function.

## Helpful links

- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [Creating a Custom Extension](https://twig.symfony.com/doc/2.x/advanced.html#creating-an-extension)

onelinerhub: [How to write PHP code in Twig?](https://onelinerhub.com/twig/how-to-write-php-code-in-twig-)