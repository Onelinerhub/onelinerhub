# How can I generate fake values using Laravel Faker?
// plain

To generate fake values using Laravel Faker, you can use the `factory()` function. This function takes two arguments: the model class and a closure that defines the fake data. The following example code will generate a fake user with a random name, email, and password:

```
$user = factory(App\User::class)->create([
    'name' => $faker->name,
    'email' => $faker->unique()->safeEmail,
    'password' => bcrypt('password'),
]);
```

The output of this code would be a new user with the random name, email, and password defined in the code.

## Code explanation


* `factory()`: This function creates a model factory for the given model class.
* `App\User::class`: This is the model class for the user.
* `create()`: This is the method used to create a new model instance.
* `$faker->name`: This generates a random name for the user.
* `$faker->unique()->safeEmail`: This generates a unique and safe email address for the user.
* `bcrypt('password')`: This hashes the given string and stores it in the database.

For more information on how to use Laravel Faker, you can refer to the [documentation](https://laravel.com/docs/master/database-testing#generating-fake-data).

onelinerhub: [How can I generate fake values using Laravel Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-fake-values-using-laravel-faker)