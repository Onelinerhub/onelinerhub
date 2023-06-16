# How do I add a column with a Laravel migration in PHP?
// plain

To add a column with a Laravel migration in PHP, you can use the `addColumn` method on the Schema facade. This method takes two parameters: the name of the table to add the column to, and an array of column properties.

For example, to add a column called `name` to the `users` table, you can use the following code:
```
Schema::table('users', function ($table) {
    $table->string('name');
});
```

The array of column properties can include the column type, length, default value, and any other relevant options. For example, to add a `price` column with a default value of `0` to the `products` table, you can use the following code:

```
Schema::table('products', function ($table) {
    $table->decimal('price', 8, 2)->default(0);
});
```

## Code explanation

- `Schema`: the facade for interacting with the database
- `table`: the method used to specify the table to add the column to
- `string` / `decimal`: the type of column to add
- `8, 2`: the length of the column (for a decimal column)
- `default`: the method used to specify a default value for the column

## Helpful links
- [Laravel Database: Migrations](https://laravel.com/docs/7.x/migrations)
- [Schema Builder](https://laravel.com/docs/7.x/migrations#schema-builder)

onelinerhub: [How do I add a column with a Laravel migration in PHP?](https://onelinerhub.com/php-laravel/how-do-i-add-a-column-with-a-laravel-migration-in-php)