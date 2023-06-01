# How do I generate realistic city names using PHP Faker?
// plain

Generating realistic city names with PHP Faker is easy. PHP Faker is a library that generates fake data for you. To generate a realistic city name, you can use the `$faker->city` method. The following example code will generate a random city name:

```php
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->city;
```

## Output example

```
Uptonbury
```

The `$faker->city` method takes two optional parameters: `$countryCode` and `$state`. `$countryCode` is a two-letter ISO 3166-1 alpha-2 country code, and `$state` is the full name of the state. For example, if you want to generate a city name from the USA, you can use the following code:

```php
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->city('US', 'New York');
```

## Output example

```
New York City
```

## Code explanation

- `require_once 'vendor/autoload.php';` - This line loads the Faker library.
- `$faker = Faker\Factory::create();` - This line creates a new Faker instance.
- `echo $faker->city;` - This line generates a random city name.
- `echo $faker->city('US', 'New York');` - This line generates a city name from the USA, specifically from the state of New York.

## Helpful links
- [PHP Faker Documentation](https://github.com/fzaninotto/Faker)
- [ISO 3166-1 alpha-2 Country Codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

onelinerhub: [How do I generate realistic city names using PHP Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-realistic-city-names-using-php-faker)