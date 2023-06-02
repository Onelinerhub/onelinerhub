# How can I generate a random number between two values using PHP Faker?
// plain

Using the [PHP Faker library](https://github.com/fzaninotto/Faker), you can generate a random number between two values using the `numberBetween` method. This method takes two arguments, the minimum and maximum values of the range from which the random number should be generated. The following example code generates a random number between 1 and 10:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

$randomNumber = $faker->numberBetween(1, 10);

echo $randomNumber;
```

## Output example

```
2
```

The code consists of the following parts:

1. The `require_once` statement loads the Faker library.
2. The `Faker\Factory::create()` call creates an instance of the Faker class.
3. The `numberBetween` method is called on the `$faker` object, passing in the two arguments to specify the range from which the random number should be drawn.
4. The result is stored in the `$randomNumber` variable.
5. The `echo` statement prints the result to the screen.

onelinerhub: [How can I generate a random number between two values using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-random-number-between-two-values-using-php-faker)