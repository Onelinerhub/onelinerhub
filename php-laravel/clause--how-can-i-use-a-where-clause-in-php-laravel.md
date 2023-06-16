# clause

How can I use a WHERE clause in PHP Laravel?
// plain

The WHERE clause is used to filter records in a database. It is used to limit the records returned from a query. In PHP Laravel, the WHERE clause can be used to filter records in a database table.

For example, the following code block will return all records from the users table where the user id is 1:

```
$user = DB::table('users')
    ->where('id', 1)
    ->get();
```

The output of the above code will be an array of records from the users table where the user id is 1.

The code can be broken down into the following parts:

1. `DB::table('users')` - This part specifies the table from which the records should be retrieved.
2. `->where('id', 1)` - This part specifies the condition that should be used for filtering the records. In this case, the condition is that the user id should be 1.
3. `->get()` - This part specifies that the records should be retrieved from the database.

For more information on using the WHERE clause in PHP Laravel, please refer to the following links:

- [Laravel - Query Builder - WHERE](https://laravel.com/docs/7.x/queries#where-clauses)
- [Laravel - Database - Query Builder](https://laravel.com/docs/7.x/database#query-builder)

onelinerhub: [clause

How can I use a WHERE clause in PHP Laravel?](https://onelinerhub.com/php-laravel/clause--how-can-i-use-a-where-clause-in-php-laravel)