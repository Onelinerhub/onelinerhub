# How can I generate a business name using PHP Faker?
// plain

Using PHP Faker you can easily generate business names with a few lines of code.

Here is an example code block:
```
<?php
$faker = Faker\Factory::create();

echo $faker->company;
```

This code will generate an output like this:
```
Smith-Mcguire
```

The code consists of three parts:
1. `$faker = Faker\Factory::create();` - this creates a Faker instance.
2. `echo $faker->company;` - this prints out a random business name.
3. The closing `?>` tag - this is the closing tag for the PHP code.

For more information on using PHP Faker, you can check out the official documentation [here](https://github.com/fzaninotto/Faker).

onelinerhub: [How can I generate a business name using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-business-name-using-php-faker)