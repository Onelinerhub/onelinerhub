# How to use Faker with PHPUnit?
// plain

Faker is a PHP library that generates fake data for you. It can be used with PHPUnit to generate test data for your tests.

## Example code

```
<?php
use Faker\Factory;

$faker = Factory::create();

echo $faker->name;
```

## Output example

```
John Smith
```

## Code explanation

- `use Faker\Factory;` - imports the Faker library
- `$faker = Factory::create();` - creates a new Faker instance
- `echo $faker->name;` - prints a random name

## Helpful links
- [Faker Documentation](https://github.com/fzaninotto/Faker)
- [PHPUnit Documentation](https://phpunit.de/documentation.html)

onelinerhub: [How to use Faker with PHPUnit?](https://onelinerhub.com/phpunit/how-to-use-faker-with-phpunit)