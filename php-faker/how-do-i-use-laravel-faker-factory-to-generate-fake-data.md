# How do I use Laravel Faker Factory to generate fake data?
// plain

Using Laravel Faker Factory, you can easily generate fake data for testing and development. Here's an example of how to use it:

```
$factory->define(App\User::class, function (Faker $faker) {
    return [
        'name' => $faker->name,
        'email' => $faker->unique()->safeEmail,
        'password' => '$2y$10$TKh8H1.PfQx37YgCzwiKb.KjNyWgaHb9cbcoQgdIVFlYg7B77UdFm', // secret
        'remember_token' => str_random(10),
    ];
});
```

This code will create a new `App\User` factory. Whenever you call `App\User::factory()->make()`, it will generate a new fake user, with a randomly generated name, email, password, and remember token.

Here are the parts of the code and what they do:

- `$factory`: This is the global factory instance.
- `define`: This is a method on the factory instance, used to define a new factory.
- `App\User::class`: This is the model class that the factory will generate data for.
- `function (Faker $faker)`: This is the closure that defines the data that will be generated for each instance.
- `$faker->name`: This is a method on the Faker instance, used to generate a random name.
- `$faker->unique()->safeEmail`: This is a method on the Faker instance, used to generate a unique, safe email address.
- `str_random(10)`: This is a helper function used to generate a random string of 10 characters.

You can find more information about Laravel Faker Factory in the [Laravel Documentation](https://laravel.com/docs/5.8/database-testing#writing-factories).

onelinerhub: [How do I use Laravel Faker Factory to generate fake data?](https://onelinerhub.com/php-faker/how-do-i-use-laravel-faker-factory-to-generate-fake-data)