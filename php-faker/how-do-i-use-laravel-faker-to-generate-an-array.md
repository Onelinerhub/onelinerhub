# How do I use Laravel Faker to generate an array?
// plain

Using Laravel Faker to generate an array is easy and straightforward.

To start, you need to install Faker in your project.

```
composer require fzaninotto/faker
```

Then you need to include the Faker class in your code.
```
use Faker\Factory as Faker;
```

Now you can create a new instance of Faker and generate an array.

```
$faker = Faker::create();
$array = $faker->words(5);
```

This will generate an array of 5 random words.

```
Array
(
    [0] => voluptate
    [1] => eaque
    [2] => et
    [3] => voluptatem
    [4] => voluptas
)
```

You can also use other Faker methods to generate different types of data. For example, you can use `$faker->email()` to generate a random email address.

For more information about Faker, please refer to the [official documentation](https://github.com/fzaninotto/Faker).

onelinerhub: [How do I use Laravel Faker to generate an array?](https://onelinerhub.com/php-faker/how-do-i-use-laravel-faker-to-generate-an-array)