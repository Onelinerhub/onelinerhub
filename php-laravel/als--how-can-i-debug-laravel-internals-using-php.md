# als

How can I debug Laravel internals using PHP?
// plain

Debugging Laravel internals using PHP can be done by using the `xdebug` extension. This extension allows for step-by-step debugging of code and can be easily enabled in the `php.ini` file by setting `zend_extension=xdebug.so` and `xdebug.remote_enable=on`.

The `xdebug` extension can be used to step through the code and inspect variables, objects, and functions. To do this, you can set breakpoints in the code and use the `xdebug_break()` function to pause execution and inspect the state of the application.

For example, the following code will pause execution when `$foo` is equal to `bar`:

```php
if ($foo == 'bar') {
    xdebug_break();
}
```

When this code is executed, the `xdebug` extension will pause execution and allow you to inspect the state of the application.

In addition to using the `xdebug` extension, you can also use the `dd()` function to inspect the state of the application. This function prints out the contents of a variable and then exits the application. This can be useful for quickly inspecting the state of the application without having to set breakpoints.

For example, the following code will print out the contents of `$foo` and then exit the application:

```php
dd($foo);
```

## Output example

```
bar
```

These are some of the ways you can debug Laravel internals using PHP.

## Helpful links
- https://www.php.net/manual/en/book.xdebug.php
- https://laravel.com/docs/7.x/helpers#method-dd

onelinerhub: [als

How can I debug Laravel internals using PHP?](https://onelinerhub.com/php-laravel/als--how-can-i-debug-laravel-internals-using-php)