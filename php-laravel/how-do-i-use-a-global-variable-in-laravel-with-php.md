# How do I use a global variable in Laravel with PHP?
// plain

A global variable in Laravel with PHP can be used in the following way:

1. Declare the variable outside of any functions and classes. For example:
```
$globalVar = "This is a global variable!";
```

2. Use the `global` keyword in the function or class where you want to use the variable. For example:
```
function myFunction() {
    global $globalVar;
    echo $globalVar;
}

myFunction();
// Output: This is a global variable!
```

3. Use the `$GLOBALS` array to access the global variable from within a function or class. For example:
```
function myFunction() {
    echo $GLOBALS['globalVar'];
}

myFunction();
// Output: This is a global variable!
```

4. Use the `$_SERVER` array to access the global variable from within a function or class. For example:
```
function myFunction() {
    echo $_SERVER['globalVar'];
}

myFunction();
// Output: This is a global variable!
```

In Laravel, you can also access global variables from within views. For example, you can access the `$globalVar` variable in a view like this:
```
{{ $globalVar }}
```

## Helpful links
- [PHP Manual - Global Variables](https://www.php.net/manual/en/language.variables.scope.php#language.variables.scope.global)
- [Laravel Documentation - Views](https://laravel.com/docs/7.x/views)

onelinerhub: [How do I use a global variable in Laravel with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-a-global-variable-in-laravel-with-php)