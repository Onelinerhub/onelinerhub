# How can I use the Laravel WhereIn method in PHP?
// plain

The Laravel WhereIn method is a powerful tool for querying databases in PHP. It allows you to specify an array of values to search for within a specific column.

For example, if you want to find all records where the value of a column is one of a given list of values, you can use the WhereIn method like this:

```
$records = DB::table('users')
    ->whereIn('role', ['admin', 'moderator', 'member'])
    ->get();
```

This code will return all records from the `users` table where the `role` column is either `admin`, `moderator`, or `member`.

The parts of the code above are:
- `DB::table('users')`: This specifies the table to query.
- `whereIn('role', ['admin', 'moderator', 'member'])`: This specifies the column to search and the list of values to search for.
- `get()`: This executes the query and returns the results.

More information about the Laravel WhereIn method can be found in the [Laravel documentation](https://laravel.com/docs/5.7/queries#where-clauses).

onelinerhub: [How can I use the Laravel WhereIn method in PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-the-laravel-wherein-method-in-php)