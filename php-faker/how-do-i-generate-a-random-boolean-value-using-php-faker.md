# How do I generate a random boolean value using PHP Faker?
// plain

Using the [PHP Faker](https://github.com/fzaninotto/Faker) library, you can generate random boolean values with the `boolean` method. The following example code will generate a random boolean value and print it to the console:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

$randomBoolean = $faker->boolean;

echo $randomBoolean;
```

## Output example

```
true
```

The `boolean` method takes an optional parameter, `$chanceOfGettingTrue`, which is a number between 0 and 100 representing the percentage chance of getting true as the result. The default value is 50. For example, the following code will generate a random boolean value with a 70% chance of getting true:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

$randomBoolean = $faker->boolean(70);

echo $randomBoolean;
```

## Output example

```
false
```

onelinerhub: [How do I generate a random boolean value using PHP Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-random-boolean-value-using-php-faker)