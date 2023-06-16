# How do I use the "WHERE LIKE" clause in PHP Laravel?
// plain

The `WHERE LIKE` clause is used in PHP Laravel to search for specific patterns in a database table. Here is an example of how it can be used:

```
$users = DB::table('users')
            ->where('name', 'LIKE', '%John%')
            ->get();

print_r($users);
```

The above code will return all users from the `users` table whose name contains "John". The output will be an array of user objects:

```
Array
(
    [0] => stdClass Object
        (
            [id] => 1
            [name] => John Doe
            [email] => john@example.com
            [age] => 30
        )

    [1] => stdClass Object
        (
            [id] => 2
            [name] => John Smith
            [email] => johnsmith@example.com
            [age] => 25
        )
)
```

## Code explanation


- `DB::table('users')` is used to select the `users` table from the database.
- `->where('name', 'LIKE', '%John%')` is used to specify the search pattern. In this case, it will search for names containing "John".
- `->get()` is used to execute the query and return the results.

## Helpful links

- [Laravel Database: Query Builder](https://laravel.com/docs/7.x/queries)
- [MySQL LIKE Clause](https://www.w3schools.com/sql/sql_like.asp)

onelinerhub: [How do I use the "WHERE LIKE" clause in PHP Laravel?](https://onelinerhub.com/php-laravel/how-do-i-use-the--where-like--clause-in-php-laravel)