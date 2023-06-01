# How can I generate decimal numbers using PHP Faker?
// plain

To generate decimal numbers using PHP Faker, you can use the `randomFloat()` method. This method takes two parameters, the first being the minimum value and the second being the maximum value. The generated number will be a float between the two parameters. For example:

```
<?php
$faker = Faker\Factory::create();
echo $faker->randomFloat(2, 0, 10);

// Output: 8.25
```

The `randomFloat()` method takes two parameters:

- `$nbMaxDecimals`: The maximum number of decimals that will be generated.
- `$min`: The minimum value for the generated number.
- `$max`: The maximum value for the generated number.

For example, to generate a float between 0 and 10 with a maximum of 2 decimals, you would use the following code:

```
<?php
$faker = Faker\Factory::create();
echo $faker->randomFloat(2, 0, 10);

// Output: 8.25
```

For more information on the `randomFloat()` method, please refer to the [PHP Faker documentation](https://github.com/fzaninotto/Faker#fakerproviderbase-randomfloat).

onelinerhub: [How can I generate decimal numbers using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-decimal-numbers-using-php-faker)