# How can I use Laravel Eloquent Faker to generate fake data?
// plain

You can use Laravel Eloquent Faker to generate fake data by defining a model and using the factory() method provided by Eloquent Faker.

```php
$factory->define(App\User::class, function (Faker $faker) {
    return [
        'name' => $faker->name,
        'email' => $faker->unique()->safeEmail,
        'password' => '$2y$10$TKh8H1.PfQx37YgCzwiKb.KjNyWgaHb9cbcoQgdIVFlYg7B77UdFm', // secret
        'remember_token' => str_random(10),
    ];
});
```

You can then use the factory() method to generate the fake data.

```php
factory(App\User::class, 10)->create();
```

This will create 10 new users in the database with random data.

## Code explanation

- `$factory->define()`: This defines the model that will be used to generate the fake data.
- `$faker->name`: This generates a random name.
- `$faker->unique()->safeEmail`: This generates a unique email address.
- `str_random(10)`: This generates a random string of 10 characters.
- `factory()`: This is the method provided by Eloquent Faker to generate the fake data.

## Helpful links
- [Laravel Eloquent Faker](https://github.com/fzaninotto/Faker#laravel-eloquent-faker)
- [Faker Documentation](https://github.com/fzaninotto/Faker)

onelinerhub: [How can I use Laravel Eloquent Faker to generate fake data?](https://onelinerhub.com/php-faker/how-can-i-use-laravel-eloquent-faker-to-generate-fake-data)