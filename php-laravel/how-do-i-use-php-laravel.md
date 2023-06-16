# How do I use PHP Laravel?
// plain

PHP Laravel is a web development framework that makes it easier to create web applications and APIs. It is a powerful framework that provides a lot of features such as routing, authentication, and a templating system.

To use PHP Laravel, you will need to install the framework on your server. The easiest way to do this is to use the Laravel installer, which can be found at https://laravel.com/docs/7.x/installation.

Once the installation is complete, you can create a new application using the `laravel new` command. This will create a new project folder with all the necessary files and directories.

To create a simple web page, you can use the `php artisan make:controller` command. This will create a controller file that you can use to define the routes and actions for your application.

For example, if you wanted to create a page that displays a list of users, you could create a controller like this:

```
<?php

namespace App\Http\Controllers;

use App\User;

class UserController extends Controller
{
    public function index()
    {
        $users = User::all();
        return view('users.index', compact('users'));
    }
}
```

This controller will call the `User::all()` method to get all the users from the database, and then pass them to the `users.index` view.

You can also use the `php artisan make:model` command to create models for your application. Models are used to represent the data in your application, and they are used to create, read, update, and delete data from the database.

Finally, you can use the `php artisan serve` command to start the development server. This will allow you to test your application in your browser.

## Helpful links

- [Laravel Documentation](https://laravel.com/docs/7.x)
- [Laravel Installation Guide](https://laravel.com/docs/7.x/installation)
- [Laravel Controllers](https://laravel.com/docs/7.x/controllers)
- [Laravel Models](https://laravel.com/docs/7.x/eloquent)

onelinerhub: [How do I use PHP Laravel?](https://onelinerhub.com/php-laravel/how-do-i-use-php-laravel)