# How can I generate a UUID using PHP Faker?
// plain

The [PHP Faker Library](https://github.com/fzaninotto/Faker) provides a convenient way to generate a UUID using the `$faker->uuid` method.

## Example code

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->uuid . "\n";
```

## Output example

```
3f8b8b7c-7e6f-3c7d-a7f3-a2f1b5f2f9c3
```

The code above uses the `require_once` command to include the autoloaded library, then it creates an instance of the `Faker\Factory` class, and finally it outputs a UUID using the `$faker->uuid` method.

The output of the code is a UUID in the format of `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`, where each `x` is a hexadecimal digit.

The `$faker->uuid` method also accepts an optional argument, which is a version number from 1 to 5. This argument affects the output of the UUID, as the version number determines the number of bits used for the various parts of the UUID.

For more information about the PHP Faker Library, please refer to the [official documentation](https://github.com/fzaninotto/Faker#fakerprovideruuid).

onelinerhub: [How can I generate a UUID using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-uuid-using-php-faker)