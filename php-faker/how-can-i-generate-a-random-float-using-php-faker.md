# How can I generate a random float using PHP Faker?
// plain

Using [PHP Faker](https://github.com/fzaninotto/Faker) library, you can generate a random float with the following code:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->randomFloat(2, 0, 100);
```

The output of the above code will be a random float with 2 digits after the decimal point, ranging from 0 to 100.

The code consists of the following parts:

1. `require_once 'vendor/autoload.php';` - This imports the Faker library.
2. `$faker = Faker\Factory::create();` - This creates an instance of the Faker library.
3. `echo $faker->randomFloat(2, 0, 100);` - This generates a random float with 2 digits after the decimal point, ranging from 0 to 100.

For more information, you can refer to the [Faker documentation](https://github.com/fzaninotto/Faker#fakerproviderbase).

onelinerhub: [How can I generate a random float using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-random-float-using-php-faker)