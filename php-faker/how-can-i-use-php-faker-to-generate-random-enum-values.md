# How can I use PHP Faker to generate random enum values?
// plain

PHP Faker is a library that can be used to generate fake data for a variety of applications. It can be used to generate random enum values as well. The Faker library provides a `randomElement()` method which can be used to generate random enum values.

## Example code

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

// Generate a random enum value
$randomEnumValue = $faker->randomElement(['value1', 'value2', 'value3']);

echo $randomEnumValue;
```

## Output example
 `value2`

The code above uses the `randomElement()` method of the Faker library to generate a random enum value. This method takes an array of enum values as a parameter, and returns a random element from the array. In this example, the array contains three enum values (`value1`, `value2`, and `value3`), and the `randomElement()` method returns a random value from that array.

## Helpful links
- [GitHub - fzaninotto/Faker: Faker is a PHP library that generates fake data for you](https://github.com/fzaninotto/Faker)
- [Faker\Generator::randomElement — Faker](https://github.com/fzaninotto/Faker#fakergeneratorrandomelement)

onelinerhub: [How can I use PHP Faker to generate random enum values?](https://onelinerhub.com/php-faker/how-can-i-use-php-faker-to-generate-random-enum-values)