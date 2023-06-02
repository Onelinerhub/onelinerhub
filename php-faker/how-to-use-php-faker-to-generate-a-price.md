# How to use PHP Faker to generate a price?
// plain

PHP Faker is a library that can be used to generate fake data for testing and development purposes. It can be used to generate a price with the following steps:

1. Install the Faker library by running `composer require fzaninotto/faker` in the terminal.

2. Create an instance of the Faker class in your script:
```php
$faker = Faker\Factory::create();
```

3. Generate a random price using the `randomFloat()` method:
```php
$price = $faker->randomFloat(2, 0, 100);
echo $price;
// Output: 55.23
```

This will generate a random price with two decimal places between 0 and 100.

The full list of methods for generating fake data with Faker can be found in the [official documentation](https://github.com/fzaninotto/Faker#formatters).

onelinerhub: [How to use PHP Faker to generate a price?](https://onelinerhub.com/php-faker/how-to-use-php-faker-to-generate-a-price)