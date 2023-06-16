# How do I use Laravel seeders to populate my database with PHP?
// plain

A Laravel seeder is a class used to populate a database with data. It can be used to insert data into the database, or to generate data that can be used for testing.

Here is an example of a seeder class that can be used to populate a database with data using PHP:

```php
<?php

use Illuminate\Database\Seeder;
use App\User;

class UsersTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        User::create([
            'name' => 'John Doe',
            'email' => 'john@example.com',
            'password' => bcrypt('password')
        ]);
    }
}
```

To use this seeder, you can run the following command in the terminal:

```
php artisan db:seed --class=UsersTableSeeder
```

The output of this command should look like this:

```
Seeded: UsersTableSeeder
```

This will create a new user in the database with the name, email, and password specified in the seeder class.

For more information on Laravel seeders, please see the [Laravel documentation](https://laravel.com/docs/7.x/seeding).

onelinerhub: [How do I use Laravel seeders to populate my database with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-laravel-seeders-to-populate-my-database-with-php)