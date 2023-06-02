# How can I generate random words of a specific length using PHP Faker?
// plain

Using the [PHP Faker library](https://github.com/fzaninotto/Faker) it is possible to generate random words of a specific length. The following example code block will generate a random word with 8 characters:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->lexify('????????');

```

This will output a random word with 8 characters, for example: `VgkVYhVd`.

The code block consists of the following parts:

1. `require_once 'vendor/autoload.php';` This line includes the autoloader, which is necessary for loading the Faker library.

2. `$faker = Faker\Factory::create();` This line creates a new Faker instance.

3. `echo $faker->lexify('????????');` This line uses the `lexify` method of the Faker instance to generate a random word. The argument of the `lexify` method is a string of 8 question marks (`????????`), which will be replaced by random characters.

For more information about the `lexify` method, please refer to the [Faker documentation](https://github.com/fzaninotto/Faker#lexify).

onelinerhub: [How can I generate random words of a specific length using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-random-words-of-a-specific-length-using-php-faker)