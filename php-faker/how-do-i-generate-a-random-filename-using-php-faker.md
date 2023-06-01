# How do I generate a random filename using PHP Faker?
// plain

Using [PHP Faker](https://github.com/fzaninotto/Faker), you can generate a random filename with the following code:

```php
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

$filename = $faker->word . '.' . $faker->fileExtension;
echo $filename;

```

The above code will output a random filename in the form of a word followed by a file extension, such as `example.png`.

The code consists of the following parts:

1. `require_once 'vendor/autoload.php';` - This line includes the autoloader for PHP Faker.
2. `$faker = Faker\Factory::create();` - This line creates an instance of the Faker class.
3. `$filename = $faker->word . '.' . $faker->fileExtension;` - This line generates a random filename by combining a random word with a random file extension.
4. `echo $filename;` - This line prints the random filename to the screen.

For more information, see the [PHP Faker documentation](https://github.com/fzaninotto/Faker#fakerproviderfile).

onelinerhub: [How do I generate a random filename using PHP Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-random-filename-using-php-faker)