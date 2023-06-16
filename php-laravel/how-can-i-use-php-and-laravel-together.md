# How can I use PHP and Laravel together?
// plain

PHP and Laravel can be used together to create powerful web applications. Laravel is a PHP web framework that provides an expressive, elegant syntax for web application development. It is built on top of the Symfony framework and includes a variety of tools such as an ORM, routing, authentication, and more.

## Example code

```
<?php

use App\User;

Route::get('/users', function () {
    return User::all();
});
```

## Output example


Array of all users in the database.

The code above is an example of how to use PHP and Laravel together. It uses the Laravel Route facade to create a route that returns all users from the database using the Eloquent ORM.

The code consists of the following parts:

1. `use App\User;` - This line imports the `User` model so it can be used in the route.
2. `Route::get('/users', function () {` - This line creates a route that responds to `GET` requests to the `/users` URL.
3. `return User::all();` - This line uses the `User` model to query the database for all users and returns them as an array.
4. `});` - This line closes the route callback function.

For more information on how to use PHP and Laravel together, see the [Laravel Documentation](https://laravel.com/docs).

onelinerhub: [How can I use PHP and Laravel together?](https://onelinerhub.com/php-laravel/how-can-i-use-php-and-laravel-together)