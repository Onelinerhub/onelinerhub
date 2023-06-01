# How can I use PHP Faker to generate a random country code?
// plain

PHP Faker is a library that can be used to generate random data. It can be used to generate a random country code by using the `countryCode` method. This method takes no parameters and returns a random two-letter country code.

## Example code


```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

$countryCode = $faker->countryCode;

echo $countryCode;

```

Example output:

```
FR
```

The code above first includes the Faker library with `require_once 'vendor/autoload.php'`. Then, it creates an instance of the Faker class with `$faker = Faker\Factory::create()`. Finally, it generates a random country code with `$countryCode = $faker->countryCode` and prints it with `echo $countryCode`.

## Code explanation

- `require_once 'vendor/autoload.php'`: includes the Faker library
- `$faker = Faker\Factory::create()`: creates an instance of the Faker class
- `$countryCode = $faker->countryCode`: generates a random country code
- `echo $countryCode`: prints the generated country code

## Helpful links
- [PHP Faker documentation](https://github.com/fzaninotto/Faker#fakerprovidercountry)
- [Faker GitHub page](https://github.com/fzaninotto/Faker)

onelinerhub: [How can I use PHP Faker to generate a random country code?](https://onelinerhub.com/php-faker/how-can-i-use-php-faker-to-generate-a-random-country-code)