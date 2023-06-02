# How can I generate a fake timestamp using PHP Faker?
// plain

Using [PHP Faker](https://github.com/fzaninotto/Faker) you can generate a fake timestamp with the following code:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->dateTimeThisMonth->format('Y-m-d H:i:s') . "\n";

```

## Output example

```
2020-08-05 15:49:59
```

The code consists of the following parts:

1. `require_once 'vendor/autoload.php'` - this loads the Faker library.
2. `$faker = Faker\Factory::create();` - this creates a new Faker instance.
3. `echo $faker->dateTimeThisMonth->format('Y-m-d H:i:s') . "\n"` - this generates a random timestamp for the current month and formats it in the Y-m-d H:i:s format.

You can find more information about generating timestamps with PHP Faker in the [official documentation](https://github.com/fzaninotto/Faker#date-and-time).

onelinerhub: [How can I generate a fake timestamp using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-fake-timestamp-using-php-faker)