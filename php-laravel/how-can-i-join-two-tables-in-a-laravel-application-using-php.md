# How can I join two tables in a Laravel application using PHP?
// plain

Joining two tables in a Laravel application using PHP is a fairly straightforward task. To join two tables, you can use the `join()` method on a query builder instance. For example, if you have two tables `users` and `posts`, you can join them using the following code:

```php
$users = DB::table('users')
    ->join('posts', 'users.id', '=', 'posts.user_id')
    ->select('users.name', 'posts.title')
    ->get();
```

The output of this code will be a collection of objects containing the `name` and `title` fields from the `users` and `posts` tables, respectively.

The parts of the code are:

- `DB::table('users')`: This is the query builder instance. It represents the `users` table.
- `join('posts', 'users.id', '=', 'posts.user_id')`: This is the `join()` method which is used to join the `users` and `posts` tables. The first argument is the name of the table to be joined, the second argument is the condition for joining, and the third argument is the operator for the condition.
- `select('users.name', 'posts.title')`: This is the `select()` method which is used to select the fields to be returned from the query.
- `get()`: This is the `get()` method which is used to execute the query and return the results.

For more information, please refer to the [Laravel documentation](https://laravel.com/docs/7.x/queries#joining-tables).

onelinerhub: [How can I join two tables in a Laravel application using PHP?](https://onelinerhub.com/php-laravel/how-can-i-join-two-tables-in-a-laravel-application-using-php)