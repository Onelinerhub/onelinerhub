# How do I generate fake data in Laravel within an hour?
// plain

Generating fake data in Laravel is a great way to quickly populate a database with dummy data. Here's a step-by-step guide to generating fake data in Laravel within an hour:

1. Install the Faker package from [Packagist](https://packagist.org/packages/fzaninotto/faker).

2. Create a new factory class for the model you want to generate data for. For example, to create a factory for a User model:

```
php artisan make:factory UserFactory
```

3. Add the fields you want to generate fake data for in the factory class. For example, to generate fake names:

```php
$factory->define(App\User::class, function (Faker $faker) {
    return [
        'name' => $faker->name,
    ];
});
```

4. Generate the fake data using the factory. For example, to generate 10 users:

```
php artisan tinker

>>> factory(App\User::class, 10)->create();
```

5. Check the database to see the generated data.

This should be enough to generate fake data in Laravel within an hour.

onelinerhub: [How do I generate fake data in Laravel within an hour?](https://onelinerhub.com/php-faker/how-do-i-generate-fake-data-in-laravel-within-an-hour)