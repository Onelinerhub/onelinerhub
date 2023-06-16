# How do I use PHP Laravel Tinker to debug my code?
// plain

Debugging code in Laravel Tinker is an easy and efficient way to test out code snippets. Tinker is a REPL (read-eval-print loop) which allows you to interactively run PHP code.

To use Tinker, you can access it from the command line by running the command `php artisan tinker`:

```
$ php artisan tinker
Psy Shell v0.9.9 (PHP 7.2.5 — cli) by Justin Hileman
>>>
```

Once you are inside the Tinker console, you can execute any PHP code you want. For example, to test a function you have written:

```
>>> myFunction('example');
## Output example
 "example"
```

You can also use Tinker to access and manipulate your application's data. For example, to retrieve a user from the database:

```
>>> $user = App\User::find(1);
=> App\User {#2920
     id: 1,
     name: "John Doe",
     email: "john@example.com",
     ...
   }
```

You can also use Tinker to debug your code by setting breakpoints. For example, you can use the `dd` function to inspect the value of a variable:

```
>>> dd($variable);
## Output example

string(5) "value"
```

Tinker is a great tool for debugging your code quickly and efficiently.

## Helpful links
- [Laravel Tinker](https://laravel.com/docs/7.x/tinker)
- [PHP REPL](https://www.php.net/manual/en/features.commandline.interactive.php)
- [Debugging with dd()](https://laravel.com/docs/7.x/helpers#method-dd)

onelinerhub: [How do I use PHP Laravel Tinker to debug my code?](https://onelinerhub.com/php-laravel/how-do-i-use-php-laravel-tinker-to-debug-my-code)