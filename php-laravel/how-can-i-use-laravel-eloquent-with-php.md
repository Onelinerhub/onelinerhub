# How can I use Laravel Eloquent with PHP?
// plain

You can use Laravel Eloquent with PHP to easily interact with your database and query your data. Eloquent provides a simple ActiveRecord implementation for working with your database. Here is an example of how you can use Eloquent to query your data:

```php
$users = User::where('active', 1)->get();

foreach ($users as $user) {
    echo $user->name;
}
```

This example will get all users with an active flag set to 1 and echo out their names.

## Code explanation


- `User::where('active', 1)` - This is the Eloquent query builder which will get all users with an active flag of 1.
- `->get()` - This will execute the query and return the results.
- `foreach ($users as $user)` - This is a loop which will loop through each user.
- `echo $user->name` - This will echo out the name of the user.

Here are some helpful links for more information:

- [Laravel Eloquent Documentation](https://laravel.com/docs/7.x/eloquent)
- [Laravel Query Builder Documentation](https://laravel.com/docs/7.x/queries)

onelinerhub: [How can I use Laravel Eloquent with PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-laravel-eloquent-with-php)