# How can I generate a fake product name using PHP Faker?
// plain

Using the PHP Faker library, you can generate a fake product name with a few lines of code. Below is an example code block to generate a fake product name:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->productName;

```

The output of this example code would be a random fake product name, such as "Incredible Rubber Computer".

## Code explanation


1. `require_once 'vendor/autoload.php';`: This line of code is used to include the PHP Faker library.

2. `$faker = Faker\Factory::create();`: This line of code is used to create a Faker instance.

3. `echo $faker->productName;`: This line of code is used to generate a fake product name.

For more information about the PHP Faker library, please see the following links:

- [GitHub Repository](https://github.com/fzaninotto/Faker)
- [Documentation](https://github.com/fzaninotto/Faker#fakerprovideren_usproductname)

onelinerhub: [How can I generate a fake product name using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-fake-product-name-using-php-faker)