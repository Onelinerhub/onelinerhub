# How do I use namespaces in Laravel with PHP?
// plain

Namespaces in Laravel with PHP are used to organize code into logical groups and to prevent name collisions between different code elements. They are defined using the `namespace` keyword.

For example:
```
namespace App\Http\Controllers;

use App\User;

class UserController
{
    public function show(User $user)
    {
        return view('user.profile', ['user' => $user]);
    }
}
```
In the above example, the namespace `App\Http\Controllers` is defined, and the `User` class is imported from the `App` namespace.

## Code explanation

- `namespace App\Http\Controllers`: This defines the namespace for the code in the file.
- `use App\User`: This imports the `User` class from the `App` namespace.
- `class UserController`: This declares the `UserController` class.
- `public function show(User $user)`: This declares the `show` method which takes the `User` object as a parameter.
- `return view('user.profile', ['user' => $user])`: This returns the view `user.profile` and passes the `User` object to it.

For more information about namespaces in Laravel, please refer to the following links:
- [Laravel - Namespaces](https://laravel.com/docs/7.x/namespaces)
- [PHP - Namespaces](https://www.php.net/manual/en/language.namespaces.php)

onelinerhub: [How do I use namespaces in Laravel with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-namespaces-in-laravel-with-php)