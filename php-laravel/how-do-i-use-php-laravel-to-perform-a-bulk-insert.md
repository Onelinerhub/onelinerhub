# How do I use PHP Laravel to perform a bulk insert?
// plain

To perform a bulk insert in PHP Laravel, you can use the `insert()` method from the `DB` class. This method accepts an array of data to be inserted. For example:

```php
$data = [
    ['name' => 'John', 'age' => 30],
    ['name' => 'Jane', 'age' => 25],
    ['name' => 'Bill', 'age' => 40],
];

DB::table('users')->insert($data);
```

This will insert 3 rows into the `users` table with the given data.

Here is a breakdown of the code:

- `$data`: This is an array of data to be inserted into the table. Each element of the array is an associative array containing the column names and values to be inserted.
- `DB::table('users')`: This will get an instance of the `QueryBuilder` class for the `users` table.
- `->insert($data)`: This will insert the data into the table.

For more information, see the [Laravel Documentation](https://laravel.com/docs/5.8/queries#inserts).

onelinerhub: [How do I use PHP Laravel to perform a bulk insert?](https://onelinerhub.com/php-laravel/how-do-i-use-php-laravel-to-perform-a-bulk-insert)