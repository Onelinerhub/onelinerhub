# How can I use a seed to generate fake data with PHP Faker?
// plain

Using the [PHP Faker](https://github.com/fzaninotto/Faker) library, you can generate fake data using a seed. A seed is a number that will always generate the same random data. This is useful for testing purposes, since you can generate the same data multiple times.

To use a seed, you first need to set it with `Faker\Factory::seed($seed)`. Then, you can create a generator and use it to generate data:

```php
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

// Set seed
Faker\Factory::seed(123);

// Generate data
echo $faker->name;
```

## Output example

```
Dr. Beryl Schneider
```

The code above does the following:
1. It includes the Faker library.
2. It sets a seed with `Faker\Factory::seed($seed)`.
3. It creates a generator with `Faker\Factory::create()`.
4. It generates a name with `$faker->name`.

The seed used in this example is `123`. If you run the code again, it will generate the same name, `Dr. Beryl Schneider`.

## Helpful links
- [Faker documentation](https://github.com/fzaninotto/Faker#usage)
- [PHP Faker library](https://github.com/fzaninotto/Faker)

onelinerhub: [How can I use a seed to generate fake data with PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-use-a-seed-to-generate-fake-data-with-php-faker)