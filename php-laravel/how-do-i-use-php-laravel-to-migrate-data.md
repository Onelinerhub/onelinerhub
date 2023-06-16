# How do I use PHP Laravel to migrate data?
// plain

Using PHP Laravel to migrate data requires the use of the `Migration` class. This class is used to define the structure of the database, as well as to modify existing tables and columns.

To create a migration, use the `make:migration` command. This command will create a file in the `database/migrations` directory. The file will contain a class that extends the `Migration` class.

The following example creates a `users` table with `id`, `name`, and `email` columns:

```
php artisan make:migration create_users_table
```

The generated file will look something like this:

```
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUsersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('email')->unique();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('users');
    }
}
```

To run the migration, use the `migrate` command:

```
php artisan migrate
```

This will create the `users` table in the database.

The `Migration` class provides several methods for creating and modifying tables and columns, such as `create`, `drop`, `rename`, `addColumn`, `changeColumn`, and `dropColumn`.

For more information, see the [Laravel documentation](https://laravel.com/docs/7.x/migrations).

onelinerhub: [How do I use PHP Laravel to migrate data?](https://onelinerhub.com/php-laravel/how-do-i-use-php-laravel-to-migrate-data)