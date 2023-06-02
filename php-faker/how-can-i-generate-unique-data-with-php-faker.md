# How can I generate unique data with PHP Faker?
// plain

Using the [PHP Faker](https://github.com/fzaninotto/Faker) library, you can generate unique data in several ways.

For example, you can generate a unique name and address with the following code:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->name . "<br>";
echo $faker->address;

```

## Output example

```
Dr. Kenneth Watsica
94439 O'Kon Neck, Lake Ryleigh, NY 80729
```

You can also generate unique numbers, strings, dates, and more. For example, to generate a unique string of characters, you can use the `randomNumber` method:

```
echo $faker->randomNumber($nbDigits = 10, $strict = false);
```

## Output example

```
1078631511
```

You can also generate unique UUIDs with the `uuid` method:

```
echo $faker->uuid;
```

## Output example

```
e8a1f1b9-d9c3-3a4f-b08f-2e8b7d5f0f1c
```

You can also generate unique images, URLs, and more. For more information, please refer to the [PHP Faker documentation](https://github.com/fzaninotto/Faker).

onelinerhub: [How can I generate unique data with PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-unique-data-with-php-faker)