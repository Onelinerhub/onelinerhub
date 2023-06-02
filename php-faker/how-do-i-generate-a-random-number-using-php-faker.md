# How do I generate a random number using PHP Faker?
// plain

Using the [PHP Faker](https://github.com/fzaninotto/Faker) library, you can generate a random number in a few lines of code. Here is an example:

```php
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

$randomNumber = $faker->numberBetween(1, 10);
echo $randomNumber;
```

The output of this code would be a random number between 1 and 10.

The code consists of the following parts:

1. `require_once 'vendor/autoload.php';` - This line loads the Faker library.
2. `$faker = Faker\Factory::create();` - This line creates a new Faker instance.
3. `$randomNumber = $faker->numberBetween(1, 10);` - This line generates the random number between 1 and 10.
4. `echo $randomNumber;` - This line prints the random number.

For more information on how to use the Faker library, please refer to the [documentation](https://github.com/fzaninotto/Faker#fakerprovidernumberbetween).

onelinerhub: [How do I generate a random number using PHP Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-random-number-using-php-faker)