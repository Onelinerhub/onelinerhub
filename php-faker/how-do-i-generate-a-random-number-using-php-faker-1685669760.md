# How do I generate a random number using PHP Faker?
// plain

Using the PHP Faker library, you can generate a random number with the `numberBetween` method. The method takes two parameters: a minimum and maximum value. The code example below shows how to generate a random number between 1 and 10:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->numberBetween(1, 10);

?>
```

This code will output a random number between 1 and 10, for example `5`.

The code consists of the following parts:

1. `require_once 'vendor/autoload.php'` - this line loads the Faker library.
2. `$faker = Faker\Factory::create()` - this line creates an instance of the Faker library.
3. `echo $faker->numberBetween(1, 10)` - this line generates a random number between 1 and 10.

For more information about the `numberBetween` method, see the [PHP Faker documentation](https://github.com/fzaninotto/Faker#fakerprovidernumberbetween).

onelinerhub: [How do I generate a random number using PHP Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-random-number-using-php-faker-1685669760)