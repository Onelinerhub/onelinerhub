# How can I use the Laravel Faker model to generate fake data?
// plain

The Laravel Faker model can be used to generate fake data for testing and seeding purposes. It uses the Faker library to generate fake data such as names, addresses, and phone numbers. Here is an example of how to use it in a seeder:

```
<?php

use Illuminate\Database\Seeder;
use Faker\Factory as Faker;

class UsersTableSeeder extends Seeder
{
    public function run()
    {
        $faker = Faker::create();

        foreach(range(1,10) as $index)
        {
            DB::table('users')->insert([
                'name' => $faker->name,
                'email' => $faker->email,
                'password' => bcrypt('password'),
            ]);
        }
    }
}
```

This code will generate 10 fake users with random names, emails, and passwords.

The parts of this code are:

- `use Faker\Factory as Faker;` - This imports the Faker library into the seeder.
- `$faker = Faker::create();` - This creates an instance of the Faker library.
- `foreach(range(1,10) as $index)` - This loop will run 10 times, creating 10 fake users.
- `$faker->name` - This will generate a random name.
- `$faker->email` - This will generate a random email address.
- `bcrypt('password')` - This will hash the password string.

For more information, see the [Laravel Documentation](https://laravel.com/docs/5.7/seeding#using-model-factories) and the [Faker Documentation](https://github.com/fzaninotto/Faker).

onelinerhub: [How can I use the Laravel Faker model to generate fake data?](https://onelinerhub.com/php-faker/how-can-i-use-the-laravel-faker-model-to-generate-fake-data)