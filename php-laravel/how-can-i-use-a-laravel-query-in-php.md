# How can I use a Laravel query in PHP?
// plain

You can use a Laravel query in PHP by using the Eloquent ORM. Eloquent is an object-relational mapper (ORM) included with Laravel which allows you to query the database using PHP syntax.

Here is an example of using Eloquent to query the database:

```php
use App\User;

$users = User::where('active', 1)
              ->orderBy('created_at', 'desc')
              ->get();
```

This code will query the database for all active users, ordered by the date they were created.

The code consists of the following parts:

- `use App\User;` - This is used to include the User model in the current namespace.
- `User::where('active', 1)` - This is used to query the database for all users with an active status of 1.
- `->orderBy('created_at', 'desc')` - This is used to order the results by the date they were created, in descending order.
- `->get()` - This is used to retrieve the results from the database.

For more information, check out the [Laravel Documentation](https://laravel.com/docs/7.x/eloquent) on Eloquent.

onelinerhub: [How can I use a Laravel query in PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-a-laravel-query-in-php)