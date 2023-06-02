# How do I generate a random last name using PHP Faker?
// plain

The PHP Faker library provides an easy way to generate random last names. It can be used to generate names from different countries, regions, and cultures.

To generate a random last name using PHP Faker, you can use the following code:

```
<?php
// include Faker library
require_once 'vendor/autoload.php';

// create Faker generator
$faker = Faker\Factory::create();

// generate random last name
$lastName = $faker->lastName;

// output random last name
echo $lastName;
```

## Output example

```
Smith
```

The code above includes the Faker library, creates a Faker generator, and then generates a random last name. Finally, it outputs the generated last name.

The code consists of the following parts:

1. `require_once 'vendor/autoload.php';` - includes the Faker library.
2. `$faker = Faker\Factory::create();` - creates a Faker generator.
3. `$lastName = $faker->lastName;` - generates a random last name.
4. `echo $lastName;` - outputs the generated last name.

## Helpful links

- [Faker Library](https://github.com/fzaninotto/Faker)
- [Faker Documentation](https://github.com/fzaninotto/Faker#fakerproviderbaselastname)

onelinerhub: [How do I generate a random last name using PHP Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-random-last-name-using-php-faker)