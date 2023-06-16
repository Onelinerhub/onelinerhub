# How do I write a MySQL query in Laravel using PHP?
// plain

To write a MySQL query in Laravel using PHP, you can use the Query Builder. The Query Builder provides a convenient, fluent interface to creating and running database queries. It can be used to perform most database operations in your application and works on all supported database systems.

Here's an example of a query using the Query Builder:

```
$users = DB::table('users')->get();

foreach ($users as $user) {
    echo $user->name;
}
```

This query will get all users from the `users` table and loop through them, printing out each user's name.

The code is broken down into the following parts:

1. `DB::table('users')` - This is used to specify the table we want to query.
2. `->get()` - This is used to specify that we want to get all users from the table.
3. `foreach ($users as $user)` - This is used to loop through each user in the array of users that was returned from the query.
4. `echo $user->name` - This is used to print out each user's name.

You can find more information about the Query Builder here: https://laravel.com/docs/7.x/queries.

You can also find more information about working with databases in Laravel here: https://laravel.com/docs/7.x/database.

onelinerhub: [How do I write a MySQL query in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-write-a-mysql-query-in-laravel-using-php)