# How do I generate a random country code using PHP Faker?
// plain

The [PHP Faker](https://github.com/fzaninotto/Faker) library can be used to generate random country codes. It provides the `countryCode` method to generate a random two-letter ISO 3166-1 alpha-2 country code.

For example, the following code block will generate a random country code:

```php
<?php

require_once 'vendor/autoload.php';

$faker = \Faker\Factory::create();

echo $faker->countryCode;
```

The output of the code above could be something like `US` or `CA` or `IT`.

The code block above consists of the following parts:

1. `require_once 'vendor/autoload.php';` - This line includes the autoloader that is used to autoload all the necessary classes from the Faker library.
2. `$faker = \Faker\Factory::create();` - This line creates an instance of the Faker library.
3. `echo $faker->countryCode;` - This line uses the `countryCode` method of the Faker library to generate a random country code.

## Helpful links

- [Faker PHP Library](https://github.com/fzaninotto/Faker)
- [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

onelinerhub: [How do I generate a random country code using PHP Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-random-country-code-using-php-faker)