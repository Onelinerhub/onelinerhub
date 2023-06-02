# How can I generate fake time data using PHP Faker?
// plain

Using [PHP Faker](https://github.com/fzaninotto/Faker) you can generate fake time data easily and quickly. Here is an example code block that generates a random date and time in the past:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->dateTimeThisCentury->format('Y-m-d H:i:s');

```

## Output example

```
1962-10-16 13:09:26
```

The code consists of three parts:
1. The first part `require_once 'vendor/autoload.php';` is used to include the Faker library in the code.
2. The second part `$faker = Faker\Factory::create();` creates an instance of the Faker library.
3. The third part `echo $faker->dateTimeThisCentury->format('Y-m-d H:i:s');` generates a random date and time in the past and formats it in the specified format.

For more information about generating fake data using PHP Faker, you can visit the [official documentation](https://github.com/fzaninotto/Faker#fakerproviderdatetime).

onelinerhub: [How can I generate fake time data using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-fake-time-data-using-php-faker)