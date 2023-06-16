# How can I use Laravel Factory and Faker to generate dummy data in PHP?
// plain

Laravel Factory and Faker can be used to generate dummy data in PHP. This can be done by creating a factory class that will generate dummy data and a faker class that will provide data for the factory class.

## Example code

```
<?php

use Faker\Generator as Faker;

$factory->define(App\User::class, function (Faker $faker) {
    return [
        'name' => $faker->name,
        'email' => $faker->unique()->safeEmail,
        'password' => '$2y$10$TKh8H1.PfQx37YgCzwiKb.KjNyWgaHb9cbcoQgdIVFlYg7B77UdFm', // secret
        'remember_token' => str_random(10),
    ];
});

$user = factory(App\User::class)->make();

echo $user->name;
```
## Output example

```
John Doe
```

The code above creates a factory class for the App\User model and defines the properties of the dummy data it will generate. The $faker variable is used to generate the data for each property. The factory(App\User::class)->make() method is then used to generate the dummy data. Finally, the name property of the user is echoed out.

## Code explanation

- use Faker\Generator as Faker; - This imports the Faker class so it can be used in the factory class.
- $factory->define(App\User::class, function (Faker $faker) {...} - This creates a factory class for the App\User model and defines the properties of the dummy data it will generate.
- $faker->name - This uses the Faker class to generate a name for the user.
- $faker->unique()->safeEmail - This uses the Faker class to generate a unique and safe email for the user.
- str_random(10) - This generates a random string of 10 characters for the remember_token property of the user.
- factory(App\User::class)->make() - This generates the dummy data.
- echo $user->name - This echoes out the name of the user.

## Helpful links
- https://laravel.com/docs/7.x/database-testing#generating-factories
- https://github.com/fzaninotto/Faker

onelinerhub: [How can I use Laravel Factory and Faker to generate dummy data in PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-laravel-factory-and-faker-to-generate-dummy-data-in-php)