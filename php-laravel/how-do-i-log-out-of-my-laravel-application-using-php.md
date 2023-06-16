# How do I log out of my Laravel application using PHP?
// plain

Logging out of a Laravel application using PHP is quite simple.

First, you need to make sure that you have the Laravel framework installed and configured.

Once that is done, you can use the following code block to log out of your application:
```php
Auth::logout();
```
This will log out the currently authenticated user from the application.

Here is a breakdown of the code:
- `Auth`: This is the authentication class provided by the Laravel framework.
- `logout()`: This is the logout method that is used to log out the currently authenticated user.

If the logout is successful, the output of the code will be `null`.

For more information on authentication in Laravel, refer to the [Laravel documentation](https://laravel.com/docs/7.x/authentication).

onelinerhub: [How do I log out of my Laravel application using PHP?](https://onelinerhub.com/php-laravel/how-do-i-log-out-of-my-laravel-application-using-php)