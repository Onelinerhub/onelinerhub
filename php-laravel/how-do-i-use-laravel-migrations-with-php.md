# How do I use Laravel migrations with PHP?
// plain

Migrations are a great way to keep track of the changes made to the database and make it easier to share the same database structure between different development environments.

In Laravel, migrations are stored in the `database/migrations` directory. Each migration file contains a up and down method, which are used to apply and rollback the changes to the database.

For example, to create a new table in the database, we can use the following code:

```
public function up()
{
    Schema::create('table_name', function (Blueprint $table) {
        $table->increments('id');
        $table->string('name');
        $table->timestamps();
    });
}
```

The up method will create a new table named `table_name` with an `id` column and a `name` column. The `timestamps` method will create two additional columns, `created_at` and `updated_at`.

To apply the migration, we can run the following command:

```
php artisan migrate
```

This will create the `table_name` table in the database.

To rollback the migration, we can use the following command:

```
php artisan migrate:rollback
```

This will drop the `table_name` table from the database.

For more information on Laravel migrations, please refer to the [official documentation](https://laravel.com/docs/7.x/migrations).

onelinerhub: [How do I use Laravel migrations with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-laravel-migrations-with-php)