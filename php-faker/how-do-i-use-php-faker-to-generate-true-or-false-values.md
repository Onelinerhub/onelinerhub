# How do I use PHP Faker to generate true or false values?
// plain

Using PHP Faker to generate true or false values is easy. Here is an example code block to generate a random boolean value:

```
<?php
// include the Faker autoloader
require_once '/path/to/Faker/src/autoload.php';

// create a Faker\Generator instance
$faker = Faker\Factory::create();

// generate a boolean value
$boolean = $faker->boolean;

echo $boolean;
```

The output of this example code would be either `true` or `false`.

## Code explanation


1. `require_once '/path/to/Faker/src/autoload.php';`: This line includes the Faker autoloader which is needed for the Faker library to work.

2. `$faker = Faker\Factory::create();`: This line creates a new Faker\Generator instance.

3. `$boolean = $faker->boolean;`: This line generates a random boolean value.

4. `echo $boolean;`: This line prints out the boolean value.

For more information, please refer to the official documentation:

- [Faker Documentation](https://github.com/fzaninotto/Faker#fakerproviderboolean)

onelinerhub: [How do I use PHP Faker to generate true or false values?](https://onelinerhub.com/php-faker/how-do-i-use-php-faker-to-generate-true-or-false-values)