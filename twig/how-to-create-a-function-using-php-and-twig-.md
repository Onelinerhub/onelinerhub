# How to create a function using PHP and Twig?
// plain

Creating a function using PHP and Twig is a simple process. The following example code block shows how to create a function that takes a string as an argument and returns the string with the first letter capitalized:
```
<?php
$twig->addFunction(
    new Twig_SimpleFunction('capitalize', function ($string) {
        return ucfirst($string);
    })
);
```
The output of this code would be the string with the first letter capitalized:
```
Input: hello
## Output example
 Hello
```
The code consists of the following parts:

1. `$twig->addFunction`: This is a method of the Twig class that adds a function to the Twig environment.
2. `new Twig_SimpleFunction`: This creates a new Twig_SimpleFunction object, which is used to create a function.
3. `'capitalize'`: This is the name of the function.
4. `function ($string)`: This is the function definition, which takes a string as an argument.
5. `return ucfirst($string)`: This is the code that is executed when the function is called. It returns the string with the first letter capitalized.

## Helpful links

- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [PHP Documentation](https://www.php.net/manual/en/index.php)

onelinerhub: [How to create a function using PHP and Twig?](https://onelinerhub.com/twig/how-to-create-a-function-using-php-and-twig-)