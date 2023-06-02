# How do I use Laravel Faker Seeder to create dummy data?
// plain

Using Laravel Faker Seeder, you can easily create dummy data for your database.

1. Install the Faker package via Composer
```
composer require fzaninotto/faker
```

2. Create a new seeder class

Create a new seeder class in your database/seeds directory, and add the following code to the class:
```
<?php

use Illuminate\Database\Seeder;
use Faker\Factory as Faker;

class UsersTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $faker = Faker::create();
    }
}
```

3. Add dummy data

Inside the run() method, you can add code to generate dummy data. For example, to generate fake users:
```
<?php

use Illuminate\Database\Seeder;
use Faker\Factory as Faker;

class UsersTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $faker = Faker::create();
        foreach (range(1,50) as $index) {
            DB::table('users')->insert([
                'name' => $faker->name,
                'email' => $faker->email,
                'password' => bcrypt('password'),
            ]);
        }
    }
}
```

4. Call the seeder class

To call the seeder class, you can use the db:seed Artisan command:
```
php artisan db:seed --class=UsersTableSeeder
```

5. Verify the dummy data

You can verify the dummy data by running a SELECT query on the users table:
```
SELECT * FROM users;
```

For more information, please refer to the [Laravel Documentation](https://laravel.com/docs/6.x/seeding) and the [Faker Documentation](https://github.com/fzaninotto/Faker).

onelinerhub: [How do I use Laravel Faker Seeder to create dummy data?](https://onelinerhub.com/php-faker/how-do-i-use-laravel-faker-seeder-to-create-dummy-data)