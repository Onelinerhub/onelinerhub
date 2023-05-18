# How to use global variables in WordPress using PHP?
// plain

Using global variables in WordPress using PHP is a great way to store and access data across multiple pages. To use global variables, you need to use the `global` keyword in the function where you want to use the variable. For example:

```
function my_function() {
global $my_variable;
$my_variable = 'Hello World!';
echo $my_variable;
}
```

## Output example

```
Hello World!
```

The code above declares a global variable `$my_variable` and assigns it a value of `Hello World!`. The `global` keyword allows the variable to be accessed from outside the function.

## Code explanation

- `global` keyword: used to declare a variable as global, allowing it to be accessed from outside the function
- `$my_variable`: the name of the global variable
- `$my_variable = 'Hello World!';`: assigns the value of `Hello World!` to the global variable
- `echo $my_variable;`: prints the value of the global variable

## Helpful links
- [Global Variables in PHP](https://www.php.net/manual/en/language.variables.scope.php)
- [Using Global Variables in WordPress](https://www.wpbeginner.com/wp-tutorials/how-to-use-global-variables-in-wordpress/)

onelinerhub: [How to use global variables in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-use-global-variables-in-wordpress-using-php)